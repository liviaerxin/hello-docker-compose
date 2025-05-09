# Handing OOM in containerized ML serving: one model worker per container

Here is a simple example of a production-ready containerized inference server to handle ML errors like OOM scalably by:

- OOM detection and graceful shutdown
- Docker auto-restart on crash
- Simple REST API with FastAPI
- Model reload support if needed

The key is to throw the error to the main process and let the container restart policy handle it. This way, the container will be restarted and the model will be reloaded.

## How to run

### For Docker Compose

```sh
docker compose up
```

Visit [http://localhost:8088/docs](http://localhost:8088/docs) to see the API documentation and test the API.

### For Kubernetes(minikube)

First, start minikube, then run the following commands:

```sh
eval $(minikube docker-env)
docker compose build
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get pods
kubectl get svc
kubectl logs -l io.kompose.service=inference-server
```

Then, to access the service by `port-forward`:

```sh
kubectl port-forward svc/inference-server 8088:8088
```

Visit [http://localhost:8088/docs](http://localhost:8088/docs) to see the API documentation and test the API.

Or to access the service by `minikube service` via **NodePort**:

```sh
minikube service inference-server --url 
```

Or to access the service by `ingress`:

```sh
kubectl apply -f ingress.yaml
kubectl get ingress
# [Optional]For Docker Desktop
minikube tunnel
```

Finally, to delete the deployment:

```sh
kubectl delete -f .
```