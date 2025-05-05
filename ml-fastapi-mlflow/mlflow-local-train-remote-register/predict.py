import mlflow.pytorch
import torch
import numpy as np

MODEL_NAME = "SimpleLinearModel"
MODEL_VERSION = 1

mlflow.set_tracking_uri("file:./mlruns")
# You can find the run_id from the output of the training script, or inspect mlruns/ folder.
model_uri = f"file:./mlruns/0/e4a37328c65846f7932723d3dcdaf9a4/artifacts/model"
model_uri = f"models:/{MODEL_NAME}/{MODEL_VERSION}"
# `pytorch`
model = mlflow.pytorch.load_model(model_uri)

# Dummy input (1 features)
X_test = torch.tensor([[5.0], [6.0]], dtype=torch.float32)
pred = model(X_test).detach().numpy()
print("Predicted logits:", pred)


# `pyfunc` generic
model = mlflow.pyfunc.load_model(model_uri)
pred = model.predict(np.array([9.0], dtype=np.float32))
print("Predicted logits:", pred)
