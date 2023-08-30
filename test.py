import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from flask import Flask, request, jsonify

model_id = "stabilityai/stable-diffusion-2-1"

# Use the DPMSolverMultistepScheduler (DPM-Solver++) scheduler here instead
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data['prompt']
    image = pipe(prompt).images[0]

    return jsonify({'image': image}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)