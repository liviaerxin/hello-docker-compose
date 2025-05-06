"""
uvicorn main:app --host 0.0.0.0 --port 8088
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mlflow.pyfunc
import numpy as np
import os

# Load model from MLflow model registry (Production stage)
MODEL_NAME = "SimpleLinearModel"
MODEL_STAGE = "Production"
mlflow.set_tracking_uri(os.environ.get("MLFLOW_SERVER", "http://127.0.0.1:5000"))
model = mlflow.pyfunc.load_model(f"models:/{MODEL_NAME}/{MODEL_STAGE}")

app = FastAPI()


# Input schema
class NumInput(BaseModel):
    inputs: list[list[float]]  # e.g., [[5.1], [3.5], [1.4,] [0.2]]


@app.post("/predict")
def predict(data: NumInput):
    try:
        # model.predict(np.array([[1], [10]], dtype=np.float32))
        inputs = np.array(data.inputs, dtype=np.float32)
        # inputs = np.array([[1], [10]], dtype=np.float32)
        preds = model.predict(inputs)
        return {"predictions": preds.tolist()}  # np.array to list
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
