# MLops: MLflow Local Training → Remote Registry → FastAPI Backend Model Serving

Why local training?

It makes the model development more efficient as:

1. Avoid Downtime Issues
2. Remote MLflow tracking server are not accessible or bad network
3. security issues.

## Overview

1. Train ML models locally, log runs and metrics to local filesystem, and register trained models to a remote MLflow server.
2. Web API server pulls the remote model for inference.

Experiment projects using `docker-compose` for simplicity running on local machine.

## Steps

1. Make sure the remote MLflow server is online.

```sh
docker-compose up -d mlflow-server minio createbuckets 
```

2. Go to [mlflow-local-train-remote-register/README.md](./mlflow-local-train-remote-register/README.md) to train model locally then register to the remote.

3. Start the inference server.

```sh
docker-compose up -d inference-server
```

4. Test the inference,

```sh
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "inputs": [
    [
      6
    ]
  ]
}'


{
  "predictions": [
    [
      10.298975944519043
    ]
  ]
}
```

Visit Inference Server UI at: `http://localhost:8000`
Visit MLflow UI at: `http://localhost:5000`
MinIO Console: `http://localhost:9001`