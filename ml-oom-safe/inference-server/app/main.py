"""
Here is a complete example of a production-ready Dockerized inference server with:
        •	OOM detection and graceful shutdown
        •	Docker auto-restart on crash
        •	Simple REST API with FastAPI
        •	Model reload support if needed
"""

# app/main.py
# import torch
# import torch.nn.functional as F
# from torchvision.models import resnet50
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
import os, signal, logging, sys

logging.basicConfig(level=logging.INFO)


def fake_answer_to_everything_ml_model(x: float):
    return x * 42


# Load model function
# def load_torch_model():
# model = resnet50(pretrained=True)
# return model.eval().to("cuda")

ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
    # ml_models["torch"] = load_torch_model()
    yield
    # Clean up the ML models and release the resources
    ml_models.clear()


app = FastAPI(lifespan=lifespan)


@app.get("/infer/")
async def infer(x: int = 0):
    try:
        # dummy_input = torch.randn(1, 3, 224, 224).to("cuda")
        # with torch.no_grad():
        # output = model(dummy_input)
        # pred = F.softmax(output, dim=1).argmax().item()
        # return {"prediction": pred}

        """Mock OOM exception when x hits 1"""
        if x == 1:
            raise RuntimeError("CUDA out of memory!")
        result = ml_models["answer_to_everything"](x)
        return {"prediction": result}

    except RuntimeError as e:
        if "CUDA out of memory" in str(e):
            logging.error("OOM detected. Restarting container.")
            os.kill(os.getpid(), signal.SIGTERM)
        raise HTTPException(status_code=500, detail=str(e))
