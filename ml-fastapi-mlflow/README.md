# MLflow Local Training → Remote Registry

Avoid downtime issues: remote tracking MLflow server not reachable.

```sh
mlflow-local-train-remote-register/
├── train.py
├── register_remote.py
├── requirements.txt
├── README.md
└── mlruns/  # Auto-created after training locally
```

## Overview

Train ML models locally, log runs and metrics to local filesystem, and register trained models to a remote MLflow server.

## Steps

1. Run `train.py` to log locally.
2. Update the `artifact_uri` in `register_remote.py`.
3. Run `register_remote.py` to push to remote MLflow.

## Setup

```bash
pip install -r requirements.txt
python train.py
python predict.py
python register_remote.py
```

---

Make sure the remote MLflow server is online and artifact access is configured correctly.

## Docker Setup (Optional)

```bash
docker-compose up -d
```
Visit MLflow UI at: `http://localhost:5000`
MinIO Console: `http://localhost:9001`

To configure MinIO as the artifact store:
- Create a bucket named `mlflow-artifacts`
- Use credentials: `minioadmin:minioadmin`