import mlflow
import mlflow.pytorch
from mlflow.tracking import MlflowClient
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

mlflow.set_tracking_uri("file:./mlruns")  # Logs everything locally, default is `file:./mlruns`

MODEL_NAME = "SimpleLinearModel"
artifact_path = "model"

# --- 1. Training Data ---
# y = 2x + 1
X_train = torch.tensor([[1.0], [2.0], [3.0], [4.0]], dtype=torch.float32)
y_train = torch.tensor([[3.0], [5.0], [7.0], [9.0]], dtype=torch.float32)


# --- 2. Define Model ---
class SimpleNet(nn.Module):
    def __init__(self, input_dim, output_dim):
        super().__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        return self.linear(x)


# --- 3. Train inside MLflow run ---
with mlflow.start_run() as run:
    model = SimpleNet(1, 1)

    # --- 3.1. Loss and Optimizer ---
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    # --- 3.2. Training Loop ---
    for epoch in range(10):
        model.train()
        optimizer.zero_grad()
        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        loss.backward()
        optimizer.step()

    # --- 3.3. Log metrics and model, Register model locally ---
    mlflow.log_param("lr", 0.01)
    mlflow.log_metric("loss", loss.item())
    mlflow.pytorch.log_model(model, artifact_path=artifact_path)

model_uri = f"runs:/{run.info.run_id}/{artifact_path}"

mv = mlflow.register_model(model_uri, MODEL_NAME)
print(f"Name: {mv.name}")
print(f"Version: {mv.version}")


# # --- 3.4. Save model uri ---
model_uri = f"file:./mlruns/{run.info.experiment_id}/{run.info.run_id}/artifacts/{artifact_path}"
print(f"Model logged locally at: {model_uri}")
