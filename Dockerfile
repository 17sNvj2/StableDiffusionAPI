# 使用官方的 Python 镜像作为基础镜像
FROM python:3.9

# 将工作目录设置为 /app
WORKDIR /app

# 将当前目录下的 test.py 复制到容器的 /app 目录中
COPY test.py /app/

# 在容器中安装可能需要的依赖
RUN pip install Flask -i https://pypi.tuna.tsinghua.edu.cn/simple

# 指定容器启动时要执行的命令，这里运行 test.py
CMD ["python", "test.py"]
