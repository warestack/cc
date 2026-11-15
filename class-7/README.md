# Week 7 — Kubernetes on GCP

Deploy a containerized FastAPI app on Google Kubernetes Engine (GKE). This lab builds on the [Week 6 Docker lab](../class-6/README.md).

## Lab Route

| Activity | Outcome |
| --- | --- |
| [Set up Cloud Shell](lab/part-1.md#1-open-cloud-shell-and-select-your-project) | Select your GCP project and enable the lab APIs. |
| [Build the Docker image](lab/part-1.md#2-build-the-docker-image-and-push-it-to-artifact-registry) | Use Cloud Build and store the image in Artifact Registry. |
| [Create and connect to a GKE cluster](lab/part-1.md#3-create-and-connect-to-a-gke-autopilot-cluster) | Create an Autopilot cluster and connect with `kubectl`. |
| [Deploy and test FastAPI](lab/part-1.md#4-deploy-fastapi) | Run the app in a Pod and open it through a Kubernetes Service. |
| [Scale and update](lab/part-1.md#6-scale-the-app-and-roll-out-a-new-version) | Run two replicas and release version 2 with a rolling update. |
| [Try a public LoadBalancer](lab/part-1.md#optional-public-loadbalancer-exercise) | Give the demo app a public IP for a short test. |
| [Cleanup](lab/part-1.md#7-cleanup) | Delete your lab's Kubernetes resources, cluster and Docker repository. |

## Before You Start

- Use your course GCP project with billing enabled.
- Run the lab commands in **Cloud Shell** in the Google Cloud console.
- Use the sample app supplied in this lab. Keep your Week 5 VM and disk for [Week 8](../class-8/README.md).
- Review the [Week 6 FastAPI Dockerfile](../class-6/lab/part-2.md#3-write-the-dockerfile) if you need a refresher.

For assessed work, follow the [coursework deployment requirements](../assignment/03-testing-and-deployment.md#kubernetes-deployment-requirements) for the LoadBalancer Service, one API replica and persistent SQLite storage. Publish your versioned image to Docker Hub as specified in the brief.

> [!WARNING]
> GKE can consume cloud credit. Delete your lab resources when you finish.

[Start Week 7 Lab 1](lab/part-1.md)
