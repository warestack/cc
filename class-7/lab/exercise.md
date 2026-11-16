# Week 7 exercise — Replace a FastAPI Pod

[Week 7 overview](../README.md) · [Guided lab, step 6](part-1.md#6-scale-to-two-replicas)

Allow about 10 minutes. Do this exercise after scaling to two replicas and before starting the version 2 rollout. You will use the Deployment and internal Service you already created.

## 1. Predict and record the starting state

Write down your prediction. When you delete one Pod, what will happen to the number of ready Pods? Will the Service keep the same `CLUSTER-IP`?

In Cloud Shell, run these checks:

```bash
kubectl config current-context
kubectl -n default get deployment fastapi
kubectl -n default get pods -l app=fastapi -o wide
kubectl -n default get service fastapi
```

Continue only if the context names your own lab cluster, the Deployment shows `2/2` ready, and both Pods show `1/1` and `Running`. If the cluster is wrong, [reconnect to your lab cluster](part-1.md#3-create-and-connect-to-a-gke-standard-cluster). Save the two Pod names and the Service's `CLUSTER-IP` in your notes. `CLUSTER-IP` is the internal address assigned to the Service.

## 2. Delete one Pod and watch for its replacement

Copy the `NAME` of **one** `fastapi-…` Pod from the previous output. Replace `your-fastapi-pod-name` with that exact name. Keep the second Pod running.

```bash
OLD_POD=your-fastapi-pod-name
kubectl -n default delete pod "$OLD_POD" --wait=false
```

If the command says `NotFound`, list the Pods again and check the spelling. Proceed after Kubernetes accepts the deletion:

```bash
kubectl -n default get pods -l app=fastapi --watch
```

You may see the old Pod marked `Terminating` and the replacement marked `Pending` or `ContainerCreating`. If the replacement is fast, you may first see both current Pods already running. The Deployment still calls for two replicas, so its ReplicaSet creates a new Pod to restore that count. Press **Ctrl+C** when the replacement shows `1/1` and `Running`, or if it still is not ready after a few minutes. The watch prints updates as new lines. Use the fresh list in the next section to see which Pods still exist.

## 3. Verify the Service and explain the result

```bash
kubectl -n default get pods -l app=fastapi -o wide
kubectl -n default get service fastapi
kubectl -n default describe endpointslices -l kubernetes.io/service-name=fastapi
```

Check that the old Pod has gone and both current Pods show `1/1` and `Running`. Under **Endpoints**, find the two current Pods by `TargetRef` or by matching their IPs. Both should show `Ready: true`. If the old Pod is still terminating or the endpoint list has yet to catch up, wait a few seconds and rerun the checks.

Record the original Pod name you deleted, the name of its replacement, and the `CLUSTER-IP` before and after. In one or two sentences, explain which resource restored the replica count and why a client can still use the same Service address.

If the replacement stays `Pending` or never reaches `1/1`, run `kubectl -n default describe pods -l app=fastapi` and look at **Events** for the replacement Pod. Keep the other Pod running and ask your tutor for help before moving on.

An open `kubectl port-forward` can close if it was attached to the deleted Pod. If you want to check `/health` again, open a fresh tunnel after the replacement is ready. [Browser test](part-1.md#5-test-the-api-in-your-browser)

[Continue to the version 2 rollout](part-1.md#7-roll-out-version-2) · [Clean up if you are stopping here](part-1.md#9-clean-up)
