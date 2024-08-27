FROM python:3.10.13-slim-bullseye

WORKDIR /app


COPY requirements.txt ./
RUN pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple  -r requirements.txt


COPY . .

