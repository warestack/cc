# Week 7 Homework 1 — Kubernetes practice and reflection

Allow about 30 minutes. Use your notes from the lab and the files in this repository. You can finish this homework after deleting your cloud resources. [Week 7 overview](../README.md) · [Lab cleanup](../lab/part-1.md#9-clean-up)

Prepare one note for feedback with two pieces of evidence, a YAML correction and a short reflection. Use the practice FastAPI app for your examples.

## 1. Choose two pieces of evidence

- Show your API health check from the lab. A Swagger screenshot or terminal excerpt should include HTTP `200` and `{"status":"ok"}`. [Browser check](../lab/part-1.md#5-test-the-api-in-your-browser)
- Show one change you made. Choose scaling to two replicas, seeing a replacement Pod, or rolling out `v2`. Include a detail that shows the change, such as the before-and-after Pod names or the new greeting. [Scale](../lab/part-1.md#6-scale-to-two-replicas) · [Replace a Pod](../lab/exercise.md) · [Roll out version 2](../lab/part-1.md#7-roll-out-version-2)

Give each excerpt a brief caption with the command or request, what you saw and what it demonstrates. If you missed a capture, say which result you did not record and describe what you would check. Label this as an expected result. Crop or redact account details, tokens and credentials before sharing screenshots or logs.

## 2. Diagnose a broken Service

Imagine a classmate has two FastAPI Pods that are `Running` and ready, but has applied this Service and cannot reach FastAPI through it. The Pods come from the supplied Deployment. One line in this Service is wrong. [FastAPI Deployment YAML](../lab/k8s/deployment.yaml)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: fastapi
spec:
  type: ClusterIP
  selector:
    app: courses-api
  ports:
    - name: http
      port: 80
      targetPort: http
```

1. Identify the line you would change and write its replacement in your note.
2. Point to the exact field in the Deployment that supports your fix. Explain how both Pods can be ready while the Service still cannot reach them.
3. Give one `kubectl` command you would run after applying the correction. Describe what you would expect to see if the Service now has both Pods available. Use the lab as a reference and answer on paper or in your note. [Check the Service endpoints](../lab/part-1.md#6-scale-to-two-replicas)

## 3. Reflect in 150–200 words

- Explain what decides how many copies of FastAPI should run, what happens when a running Pod disappears, and how clients keep using the same Service.
- Compare the named Docker volume from Week 6 with the PersistentVolumeClaim required for Piazza. Explain why a successful `/health` request after a Pod replacement would not, by itself, prove that SQLite data survived. [Week 6 SQLite lab](../../class-6/lab/sqlite-and-docker.md) · [Coursework deployment requirements](../../assignment/03-testing-and-deployment.md#kubernetes-deployment-requirements)

Keep your evidence, YAML correction and verification command separate from the reflection’s word count.
