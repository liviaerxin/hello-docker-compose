FROM python:3.10-slim

WORKDIR /app

RUN pip install redis
COPY data_streamer.py /app/
CMD ["python3", "data_streamer.py"]