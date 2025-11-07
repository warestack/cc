## Lab 6 Exercises — Deploying on Kubernetes

Below are a series of exercises designed to help you deepen your understanding of Kubernetes through both hands-on practice and research.
Please note that you will need to create a new Kubernetes cluster to complete these exercises and run the commands successfully.

---

### Exercise 1 — Inspect and Debug Your Pods

**Goal:** Learn how to verify and debug Kubernetes pods.

**Tasks:**

1. Run the following to see detailed information about one pod:

   ```bash
   kubectl describe pod <pod-name>
   ```

2. Check the logs of one running pod:

   ```bash
   kubectl logs <pod-name>
   ```

3. Delete one of your pods:

   ```bash
   kubectl delete pod <pod-name>
   ```

4. Observe how Kubernetes automatically replaces it to maintain the replica count.

**Question:**  
Why does Kubernetes automatically create a new pod after one is deleted?  
*Hint: Think about what the Deployment controller does.*

---

### Exercise 2 — Scale and Observe Load Balancing

**Goal:** Practice horizontal scaling and understand how load balancing distributes traffic.

**Tasks:**

1. Scale your deployment to 20 replicas:

   ```bash
   kubectl scale deployment mini-hi-deployment --replicas=20
   ```

2. Get all pods and see which nodes they are placed on:

   ```bash
   kubectl get pods -o wide
   ```

3. Open your service’s **EXTERNAL-IP** in a browser and refresh the page multiple times.

**Question:**  
What happens to your app’s response speed or behavior when you increase the number of replicas?  
Does the load balancer automatically distribute requests?

---

### Exercise 3 — Update, Roll Back, and Clean Up

**Goal:** Understand how Kubernetes manages rolling updates and rollbacks.

**Tasks:**

0. Debugging tip: To confirm requests go to multiple pods, you can temporarily modify your app to print the pod name:

    ```
    res.send('Hello from pod ' + process.env.HOSTNAME);
    ```

2. Edit your deployment to use a new image version:

   ```bash
   kubectl set image deployment/mini-hi-deployment minihi=steliosot/mini-hi:2
   ```

3. Check rollout status:

   ```bash
   kubectl rollout status deployment/mini-hi-deployment
   ```

4. View the deployment history:

   ```bash
   kubectl rollout history deployment/mini-hi-deployment
   ```

5. Roll back to the previous version:

   ```bash
   kubectl rollout undo deployment/mini-hi-deployment
   ```

6. Delete your cluster when finished to avoid costs.

**Question:**  
Why is using `rollout undo` safer than manually redeploying your previous image?

---

## Research-Based Exercises

### Exercise 4 — Kubernetes vs. Docker Swarm

**Goal:** Compare container orchestration tools.

**Tasks:**

1. Research the main differences between **Kubernetes** and **Docker Swarm** in terms of:
   - Scalability  
   - Networking  
   - Load balancing  
   - Ease of setup
2. Write a short paragraph (150–200 words) explaining when you would choose one over the other.
3. Include at least one academic or industry reference (e.g., Google Cloud Docs, Red Hat Blog, IEEE paper).

**Hint:** Focus on how Kubernetes’ declarative model differs from Swarm’s simpler architecture.

---

### Exercise 5 — Cost and Sustainability in Cloud Deployments

**Goal:** Reflect on the environmental and financial impact of using cloud clusters.

**Tasks:**

1. Research how much it typically costs to run a 3-node GKE Standard cluster for 24 hours.  
2. Estimate the annual carbon footprint of running this cluster continuously (use public cloud sustainability calculators).  
3. Suggest two ways to optimize resource usage (e.g., autoscaling, ephemeral clusters).  
4. Write a short reflective note (100–150 words):  
   *“How can DevOps teams balance performance and sustainability?”*

---

### Exercise 6 — The Role of Kubernetes in DevOps Pipelines

**Goal:** Explore how Kubernetes integrates into modern DevOps workflows.

**Tasks:**

1. Research and describe how CI/CD tools (like Jenkins, GitHub Actions, or ArgoCD) deploy to Kubernetes.  
2. Find a real-world company case study (e.g., Netflix, Shopify, or Spotify) that uses Kubernetes in production.  
3. Summarize the benefits they achieved (e.g., scalability, resilience, automation).  
4. Write a 200-word mini-report with proper referencing (Harvard style).

---

✅ **Submission Tip:**  
Add your answers, screenshots, or mini-reports under a new file called `Lab6_Exercises.md` in a new public repo and share the repo URL.  
Make sure to include code snippets and references where relevant.
