FROM python:3.10-slim

WORKDIR /app

# Install dependencies
RUN pip install mlflow

EXPOSE 5000

# Run FastAPI app
CMD  ["mlflow", "server", "--host", "0.0.0.0", "--port", "5000"]