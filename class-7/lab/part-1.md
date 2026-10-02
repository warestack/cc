### Week 7 Lab 1: Deploy FastAPI on Kubernetes with GKE

In this tutorial, you will deploy a containerised FastAPI application to Kubernetes on Google Cloud.

You will use:

- Docker to package the FastAPI app.
- Docker Hub to store the image.
- Google Kubernetes Engine, also called GKE, to run Kubernetes on GCP.
- `kubectl` to control Kubernetes.

Use your Week 5 VM or your own computer for the Docker build. Use Google Cloud Shell for the GKE and `kubectl` commands.

#### What You Will Learn

- What a Kubernetes cluster is.
- What a Pod is.
- What a Deployment is.
- What a Service is.
- How to deploy a FastAPI container to GKE.
- How to scale an app.
- How to clean up cloud resources.

> [!WARNING]
>
> GKE creates cloud resources that cost money. Delete the cluster at the end of the lab.

#### Part A: Prepare the FastAPI App

1. Create a new folder:

```bash
mkdir week7-fastapi-kubernetes
cd week7-fastapi-kubernetes
```

2. Create `requirements.txt`:

```bash
pico requirements.txt
```

3. Add:

```text
fastapi==0.141.1
uvicorn==0.52.4
```

4. Create `main.py`:

```bash
pico main.py
```

5. Add:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello from FastAPI on Kubernetes"}


@app.get("/health")
def health():
    return {"status": "ok"}
```

This is a very small FastAPI app.

- `GET /` confirms that the API is running.
- `GET /health` is a health-check endpoint.
- Kubernetes will run this app inside containers.

#### Part B: Create the Dockerfile

6. Create `Dockerfile`:

```bash
pico Dockerfile
```

7. Add:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

This file describes the image.

- `FROM` chooses the base Python image.
- `WORKDIR` sets the working folder inside the container.
- `COPY requirements.txt .` copies the dependency list.
- `RUN pip install ...` installs FastAPI and Uvicorn.
- `COPY . .` copies the app code.
- `CMD ...` starts the FastAPI server.

#### Part C: Build and Push the Image

8. Log in to Docker Hub:

```bash
docker login
```

9. Build the image.

Replace `YOUR_DOCKERHUB_USERNAME` with your Docker Hub username:

```bash
docker build -t YOUR_DOCKERHUB_USERNAME/week7-fastapi-k8s:1 .
```

Do not forget the final `.`.

10. Test the image locally:

```bash
docker run -d --name week7-api-test -p 8080:8000 YOUR_DOCKERHUB_USERNAME/week7-fastapi-k8s:1
```

11. Open:

```text
http://127.0.0.1:8080/
```

You should see:

```json
{"message":"Hello from FastAPI on Kubernetes"}
```

12. Stop and remove the test container:

```bash
docker stop week7-api-test
docker rm week7-api-test
```

13. Push the image to Docker Hub:

```bash
docker push YOUR_DOCKERHUB_USERNAME/week7-fastapi-k8s:1
```

Kubernetes needs to pull the image from somewhere. Docker Hub is the image registry we use in this lab.

#### Part D: Create a GKE Cluster

14. Open Google Cloud Console.

15. Open **Cloud Shell**.

16. Set your project:

```bash
gcloud config set project YOUR_PROJECT_ID
```

17. Enable the Kubernetes Engine API:

```bash
gcloud services enable container.googleapis.com
```

18. Create a small Standard GKE cluster:

```bash
gcloud container clusters create week7-cluster \
  --zone europe-west2-a \
  --num-nodes 2 \
  --machine-type e2-medium
```

Use a zone close to the region you used in earlier GCP labs if needed.

This command creates a Kubernetes cluster.

- A cluster is a group of machines that run containerised applications.
- GKE manages the Kubernetes control plane for you.
- The nodes are the machines where your containers run.

19. Connect `kubectl` to the cluster:

```bash
gcloud container clusters get-credentials week7-cluster \
  --zone europe-west2-a \
  --project YOUR_PROJECT_ID
```

20. Check the nodes:

```bash
kubectl get nodes
```

You should see the nodes in the cluster.

#### Part E: Create a Kubernetes Deployment

21. Create `deployment.yaml` in Cloud Shell:

```bash
pico deployment.yaml
```

22. Add this YAML.

Replace `YOUR_DOCKERHUB_USERNAME`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fastapi-deployment
  labels:
    app: fastapi-k8s
spec:
  replicas: 3
  selector:
    matchLabels:
      app: fastapi-k8s
  template:
    metadata:
      labels:
        app: fastapi-k8s
    spec:
      containers:
      - name: fastapi
        image: YOUR_DOCKERHUB_USERNAME/week7-fastapi-k8s:1
        imagePullPolicy: Always
        ports:
        - containerPort: 8000
```

This file describes the desired state of the app.

- `kind: Deployment` means Kubernetes should manage the app.
- `replicas: 3` asks Kubernetes to run three copies.
- `selector` connects the Deployment to Pods with the label `app: fastapi-k8s`.
- `image` is the Docker image Kubernetes will pull.
- `containerPort: 8000` is the port Uvicorn uses inside the container.

23. Apply the Deployment:

```bash
kubectl apply -f deployment.yaml
```

24. Check the Pods:

```bash
kubectl get pods
```

Wait until all Pods show `Running`.

25. See more detail:

```bash
kubectl get pods -o wide
```

This shows which node each Pod is running on.

#### Part F: Expose the App with a Service

26. Create `service.yaml`:

```bash
pico service.yaml
```

27. Add:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: fastapi-service
spec:
  type: LoadBalancer
  selector:
    app: fastapi-k8s
  ports:
  - name: http
    protocol: TCP
    port: 80
    targetPort: 8000
```

This file exposes the app to the internet.

- `type: LoadBalancer` asks GCP to create a public load balancer.
- `port: 80` is the public HTTP port.
- `targetPort: 8000` sends traffic to the FastAPI container port.
- `selector` connects the Service to the Pods from the Deployment.

28. Apply the Service:

```bash
kubectl apply -f service.yaml
```

29. Check the Service:

```bash
kubectl get services
```

The `EXTERNAL-IP` may say `<pending>` for a few minutes.

30. When the external IP appears, open:

```text
http://EXTERNAL_IP/
http://EXTERNAL_IP/health
```

Remember to use `http`, not `https`.

#### Part G: Scale the App

31. Scale the Deployment to 5 replicas:

```bash
kubectl scale deployment fastapi-deployment --replicas=5
```

32. Check the Pods:

```bash
kubectl get pods
```

Kubernetes should create more Pods.

33. Scale back to 2 replicas:

```bash
kubectl scale deployment fastapi-deployment --replicas=2
```

#### Part H: Update the App

34. Change the message in `main.py`:

```python
return {"message": "FastAPI version 2 running on Kubernetes"}
```

35. Build and push version 2:

```bash
docker build -t YOUR_DOCKERHUB_USERNAME/week7-fastapi-k8s:2 .
docker push YOUR_DOCKERHUB_USERNAME/week7-fastapi-k8s:2
```

36. Update the Kubernetes image:

```bash
kubectl set image deployment/fastapi-deployment \
  fastapi=YOUR_DOCKERHUB_USERNAME/week7-fastapi-k8s:2
```

37. Watch the rollout:

```bash
kubectl rollout status deployment/fastapi-deployment
```

38. Refresh the browser.

You should see the new message.

#### Part I: Cleanup

39. Delete the Service:

```bash
kubectl delete -f service.yaml
```

40. Delete the Deployment:

```bash
kubectl delete -f deployment.yaml
```

41. Delete the GKE cluster:

```bash
gcloud container clusters delete week7-cluster --zone europe-west2-a
```

Type `Y` when asked.

42. Check that the cluster is gone:

```bash
gcloud container clusters list
```

#### Checklist

Before you finish, make sure:

- your Docker image was pushed to Docker Hub
- the GKE cluster was created
- `kubectl get nodes` worked
- the Deployment created Pods
- the Service created an external IP
- the FastAPI app worked in the browser
- scaling changed the number of Pods
- the app was updated to version 2
- the Service, Deployment, and cluster were deleted

Week 7 is complete.
