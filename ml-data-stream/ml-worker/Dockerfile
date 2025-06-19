FROM python:3.10-slim

WORKDIR /app

RUN pip install torch redis numpy

COPY ml_worker.py /app/
CMD ["python3", "ml_worker.py"]