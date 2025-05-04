# Use official PyTorch image with CUDA
FROM python:3.10

WORKDIR /app

RUN pip install fastapi uvicorn

COPY app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8088"]