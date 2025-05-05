import mlflow
from mlflow.tracking import MlflowClient
import os

MODEL_NAME = "SimpleLinearModel"
MODEL_STAGE = "Production"
MODEL_VERSION = "1"

os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://127.0.0.1:9000"  # minio
os.environ["AWS_ACCESS_KEY_ID"] = "minioadmin"
os.environ["AWS_SECRET_ACCESS_KEY"] = "minioadmin"

# 1. Retrieve local model
mlflow.set_tracking_uri("file:./mlruns")
model_uri = f"models:/{MODEL_NAME}/{MODEL_VERSION}"
model = mlflow.pytorch.load_model(model_uri)

# 1. Log and Register the model
# client = MlflowClient(tracking_uri="http://127.0.0.1:5001")
# client.log_artifacts(model, artifact_path="model") # log model artifacts
# client.create_registered_model(MODEL_NAME)
# client.create_model_version(...)

# 1. Log and Register the model
mlflow.set_tracking_uri("http://127.0.0.1:5001")
mi = mlflow.pytorch.log_model(model, artifact_path="model", registered_model_name=MODEL_NAME)
model_version = mi.registered_model_version

# 2. Promote to Production
client = MlflowClient(tracking_uri="http://127.0.0.1:5001")
client.transition_model_version_stage(
    name=MODEL_NAME, version=model_version, stage=MODEL_STAGE, archive_existing_versions=True
)
