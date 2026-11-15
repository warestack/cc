from fastapi import FastAPI

app = FastAPI(title="FastAPI on Kubernetes")


@app.get("/")
def home():
    return {"message": "Hello from FastAPI on Kubernetes"}


@app.get("/health")
def health():
    return {"status": "ok"}
