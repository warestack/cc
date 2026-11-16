# Week 7 — Deploy FastAPI on Kubernetes with GKE

In Week 6 you built a FastAPI image, published it to Docker Hub and ran a container on a Google Cloud VM. This week you build a new image with Cloud Build, store it in Artifact Registry and use Google Kubernetes Engine (GKE) to run and update the containers. [Review Week 6](../class-6/README.md).

The guided lab starts with a small FastAPI app and assumes this is your first time using Kubernetes. You only need your browser and course Google Cloud project. Use the Google Cloud Console to create resources and Cloud Shell for the commands. Keep your Week 5 VM stopped with its disk for [Week 8](../class-8/README.md).

## Two-hour lab route

Choose one practice option during the lab. Allow 15 minutes for either option, then finish with cleanup.

| Activity | Time | Outcome |
| --- | ---: | --- |
| [1. Select your project and enable the APIs](lab/part-1.md#1-select-your-project-and-enable-the-apis) | 10 minutes | Find your project ID and prepare the Google Cloud services. |
| [2. Create the Docker repository](lab/part-1.md#2-create-the-docker-repository) | 5 minutes | Set up a Docker image repository in Artifact Registry. |
| [3. Create and connect to a GKE Standard cluster](lab/part-1.md#3-create-and-connect-to-a-gke-standard-cluster) | 20 minutes | Create a cluster with one worker node and check the connection in Cloud Shell. |
| [4. Build and deploy FastAPI](lab/part-1.md#4-build-and-deploy-fastapi) | 25 minutes | Publish `fastapi:v1`, then create a Deployment and an internal Service from YAML. |
| [5. Test the API in your browser](lab/part-1.md#5-test-the-api-in-your-browser) | 10 minutes | Use Cloud Shell Web Preview and FastAPI's interactive documentation to test the API. |
| [6. Scale to two replicas](lab/part-1.md#6-scale-to-two-replicas) | 10 minutes | See two Pods and find them behind the same Service. |
| [Practice option A: Replace a Pod](lab/exercise.md) | 10–15 minutes | Predict what happens when a Pod disappears, then check how the Deployment and Service respond. Do this after step 6. |
| [7. Roll out version 2](lab/part-1.md#7-roll-out-version-2) | 15 minutes | Rebuild with a new tag, update the Deployment and verify the new response. |
| [Practice option B: Step 8, try a public LoadBalancer](lab/part-1.md#8-try-a-public-loadbalancer) | 15 minutes | Test a temporary public endpoint if your project permits one. |
| [9. Clean up](lab/part-1.md#9-clean-up) | 10 minutes | Remove the resources that can consume your cloud credit. |

After cleanup, complete [Homework 1](homework/homework-1.md) using your lab notes and the supplied YAML files. Allow about 30 minutes.

Provisioning and deletion can take several minutes. You need a course Google Cloud project with billing enabled and permission to enable the required services and create lab resources. The lab uses the supplied app in this repository. Review the [Week 6 Dockerfile walkthrough](../class-6/lab/part-2.md#3-write-the-dockerfile) or [image publishing exercise](../class-6/lab/docker-hub.md#4-tag-and-push-the-existing-image) if you need a refresher.

> [!WARNING]
>
> The cluster, worker node and optional public load balancer can use cloud credit. Allow time for cleanup and confirm your resources are gone before you finish.

This practice app has no database. For your Piazza coursework, publish the image to Docker Hub and use one API replica, the `Recreate` strategy, a LoadBalancer Service and a PersistentVolumeClaim for SQLite. The SQLite data from Week 6 stays in its named volume on the VM. Follow the assessed requirements for storage, configuration, secrets and evidence. [Coursework deployment requirements](../assignment/03-testing-and-deployment.md#kubernetes-deployment-requirements).

[Start Week 7 Lab 1](lab/part-1.md) · [Instructor verification](verification.md)
