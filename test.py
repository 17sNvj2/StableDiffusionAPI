# import torch
# from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

# model_id = "./stable-diffusion-2-1"


# # Use the DPMSolverMultistepScheduler (DPM-Solver++) scheduler here instead
# pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
# pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
# pipe = pipe.to("cuda")

# prompt = "a photo of an astronaut riding a horse on mars"
# image = pipe(prompt).images[0]

# image.save("astronaut_rides_horse.png")

from flask import Flask

app = Flask(__name__)


@app.route('/hello/model')
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)