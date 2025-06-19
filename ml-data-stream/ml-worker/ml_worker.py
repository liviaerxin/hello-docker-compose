import torch
import torch.nn as nn
import torch.optim as optim
import redis
import json
import random
import time

# time.sleep(5)

print(f"Finished training model!")

def generate_training_sensor_data():
    return {
        'features': [[random.uniform(0, 1), random.uniform(0, 1)]] * 100,
        'targets': [[random.uniform(0, 1)]] * 100    # Mock target for lighting prediction
    }

training_data = generate_training_sensor_data()
X_train = torch.tensor(training_data["features"], dtype=torch.float32)
y_train = torch.tensor(training_data["targets"], dtype=torch.float32)
# Simple mock PyTorch model

class LightingModel(nn.Module):
    def __init__(self):
        super(LightingModel, self).__init__()
        self.fc = nn.Linear(2, 1)  # Mock model, 2 features, 1 output

    def forward(self, x):
        return self.fc(x)

# Mock training loop for simplicity
def train_model():
    # Define the model and optimizer
    model = LightingModel()
    
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)
    
    for epoch in range(10):
        model.train()
        optimizer.zero_grad()
        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        loss.backward()
        optimizer.step()
        
    return model

ml_model = train_model()
print(f"Finished training model!")

# Setup Redis
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)
print(f"Connected to Redis: {redis_client.ping()}")

def control_lighting(prediction):
    # Mock logic to control lighting
    if prediction > 0.5:
        print("Lights ON")
    else:
        print("Lights OFF")
        
def listen_for_inference():
    while True:
        # Listen to Redis stream for new prediction, `$` means the latest ID in the stream
        l = redis_client.xread(streams={'sensor_data': '$'}, block=0, count=1)
        for id, value in l[0][1]: # l[0][1]: messages of the first stream
            print(f"Received message: {value}")
            data = json.loads(value[b'data'])
            feature = data['feature']
            # print(f"Received message: {feature}")
            result = ml_model(torch.tensor(feature, dtype=torch.float32))
            print(f"Prediction: {result.tolist()}")
            control_lighting(result.tolist()[0])
            
listen_for_inference()