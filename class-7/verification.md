# Week 7 instructor verification

The [student lab](lab/part-1.md) was tested on 16 November 2026 in the course demonstration project. The test used the supplied FastAPI app, Dockerfile and Kubernetes manifests. Test infrastructure was provisioned with `gcloud`; the corresponding Console forms and the live resource pages were checked and captured for the handout.

| Check | Observed result |
| --- | --- |
| GKE cluster | Standard, `europe-west1-b`, GKE `1.36.4-gke.2377000`; one ready `e2-standard-2` worker with a 30 GB balanced persistent boot disk. |
| Cloud Build and Artifact Registry | Regional builds for `v1` and `v2` both reported `SUCCESS`. The Docker repository showed two tags with different image digests (`sha256:e34adf626dcf…` and `sha256:b466fe54f10e…`). |
| First deployment | Cloud Shell `kubectl` connected to the cluster. `fastapi` rolled out with one ready Pod and a ClusterIP Service on port `80` targeting `8080`. |
| Private browser preview | `/` returned the original greeting. Swagger executed `GET /health` with HTTP `200` and `{"status":"ok"}`. `/openapi.json` listed both application routes. |
| Horizontal scaling | The Deployment reached `2/2` ready. Both Pods ran on the same worker, and both of their IPs were present as ready Service endpoints. |
| Rolling update | The `v2` ReplicaSet reached two ready replicas; the `v1` ReplicaSet went to zero. A fresh Cloud Shell preview returned the v2 greeting; `/health` still returned `{"status":"ok"}`. |
| Public Service | The external endpoint served the v2 greeting, the health route and `/docs`. All 20 tagged health requests succeeded. The two Pod logs recorded 13 and 7 requests. |
| Cleanup | Removed the test public Service and its forwarding rule, the cluster and its worker, and the test Artifact Registry repository. Removed the two source archives uploaded by the test builds. |

The same FastAPI image was also built and run locally with Docker. Both application routes, Swagger UI and the OpenAPI document returned HTTP `200`; the running container used UID and GID `10001`.
