import json
import random
import time
import redis


# Setup Redis
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)


# Simulate sensor data
def generate_sensor_data():
    return {
        'feature': [random.uniform(0, 1), random.uniform(0, 1)],
        'target': random.uniform(0, 1)  # Mock target for lighting prediction
    }

# Simulate streaming data
while True:
    sensor_data = generate_sensor_data()
    payload = json.dumps(sensor_data)
    redis_client.xadd('sensor_data', {"data": payload})
    time.sleep(5)