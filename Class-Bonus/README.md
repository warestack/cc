###  Bonus Lab: Deploying on Kubernetes

#### What am I about to learn?

Today's lab session focused on Kubernetes! We will create a new Kubernetes cluster and deploy a containerised application.

Bonus Lab focuses on how to:

* Deploy Kubernetes on the Google Kubernetes Engine (GKE) in GCP
* Run the basic commands to interact with push Docker images on the Docker Hub
* Deploy images from DockerHub to Kubernetes
* Horizontal scaling of images to support increased traffic using a load balancing service.

You will need to watch the following video to follow the step by step commands.

> Take your time; make sure you double-check the commands before you run them.

* The following video demonstrates the commands used in this tutorial. 

[![Watch the video](https://i.ytimg.com/vi/LS0UvkbA9Pw/hqdefault.jpg)](https://youtu.be/LS0UvkbA9Pw)

> **You should run this tutorial on your GCP VM and the  Google Cloud Shell :white_check_mark:**

* To run this tutorial, you will need a GCP VM; you must use the docker VM that we created in Lab 5.

1. Let's start! Firstly, go to DockerHub and create a new account; we will use Docker Hub to push our images to deploy on Kubernetes.
   * The link to Docker Hub: [DockerHub](https://hub.docker.com/)
2. Create a new public repository. 
   * Add a name and a description; your Docker Hub username is on the top right corner of your screen.

![dockerhub](images/dockerhub.png)

3. Go back to your Docker VM (from lab 5) and log in to Docker Hub using your docker user.

* If you deleted your VM, go on and create a new one, and then install docker.

```bash
$ docker login -u steliosot
```

> In the VM, do not forget to switch to `docker-user`. The command is `su - docker-user; we ensure that we log in and switch to the docker-user home directory using the option.

4. Feel free to use the mini-hi repo, or create your own.

* If you create your application, you will need to create a new repo, push your code, and clone it in the VM.
* In my case, I used the public: `mini-hi.git`, if you like, go on and examine it.

```bash
$ git clone --branch master https://github.com/steliosot/mini-hi.git
```

> If you want, you can install Docker on your own computer
>
> * Link to Docker desktop: [Docker desktop](https://docs.docker.com/get-docker/) and push your image from your own computer, rather than moving everything to the VM.
>
> The `mini-hi` app is nothing more than a simple node.js server with a Hello World message, my `app.js` looks like this.
>
> ```javascript
> const express = require('express')
> const app = express()
> 
> app.get('/',(req,res)=>{
>     res.send('Hello World! Cloud@Birkbeck is fun!')    
> })
> 
> app.listen(3000)
> ```

5. Let's start!

```bash
$ cd mini-hi/
```

6. The Dockerfile is already there (I created it for you :happy:), so let's examine it.

```dockerfile
$ cat Dockerfile

FROM alpine
RUN apk add --update nodejs npm
COPY . /src
WORKDIR /src
EXPOSE 3000
ENTRYPOINT ["node", "./app.js"]
```

> Usual stuff... :ok:

7. Let's `build` our image.

* The image name format should be the following:
  * **<DockerHub-username>/<image-name>:<version>**
  * Make sure you change the following command and don't forget the `.` (dot) in the end (I always do).

```bash
$ docker image  build -t steliosot/mini-hi:1 .
```

8. Let's `push` our image to the DockerHub.

```bash
$ docker push steliosot/mini-hi:1

The push refers to repository [docker.io/steliosot/mini-hi]
c286528ccc74: Pushed 
03065d34267b: Pushed 
8d3ac3489996: Mounted from library/alpine 
1: digest: sha256:0c9e3709378e9898234377430d34 size: 951
```

9. Go back to your DockerHub and refresh your page; your image should be there now!

10. Let's find it using the `docker search` command and your username.

```bash
$ sudo docker search steliosot

NAME    	DESCRIPTION        		STARS     OFFICIAL   AUTOMATED
steliosot/mini-hi   A hello world container using node.js (cloud…   0 
```

* 0 stars yet :disappointed: but its a start :stuck_out_tongue:

11. Now let's move to Kubernetes.

12. Create a Kubernetes cluster (GKE Standard) using the GKE.

* You will only need to provide a meaningful name, e.g. *my-gke-cluster*
* By default, we will deploy **3** nodes.
* This might take some time, so sit tight!

13. Activate the Cloud Shell, and let's try to deploy our app in Kubernetes!

14. Firstly, let's connect to the Kubernetes cluster, click on the cluster name and then on the connect button and copy the long command. It looks like this:

```bash
$ gcloud container clusters get-credentials stelios-cluster13 --zone us-central1-c --project lab-7-270015
```

* What is `gcloud`?
  * The Google Cloud CLI is a set of tools to create and manage Google Cloud resources [[gcloud CLI overview](https://cloud.google.com/sdk/gcloud)]. 

15. Run the command in the **Cloud Shell**, click yes on the **Authorize ...** popup window.

16. Now we are connected to the Kubernetes cluster, let's run a couple of commands.

```bash
$ kubectl get nodes
```

17. Let's try the following command to extract cluster information:

```bash
$ kubectl cluster-info

Kubernetes control plane is running at https://34.123.142.19
GLBCDefaultBackend is running at https://34.123.142.19/api/v1/namespaces/kube-system/services/default-http-backend:http/proxy
KubeDNS is running at https://34.123.142.19/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
Metrics-server is running at https://34.123.142.19/api/v1/namespaces/kube-system/services/https:metrics-server:/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
```

18. Let's try to run a container of the `mini-hi` image. :ok:, get ready for it!

```bash
$ kubectl run mini-hi-pod --image=steliosot/mini-hi:1
```

19. Let's check if this is ready.

```bash
$ kubectl get pods

NAME          READY   STATUS    RESTARTS   AGE
mini-hi-pod   1/1     Running   0          69s
```

> This might take a minute so, we need to wait until we see it `Running`. So repeat the command a couple of more times.

20. Let's see some information about the running pod.

```bash
$ kubectl describe pods

...
Status:       Running
IP:           10.104.2.7
...
```

> There is a lot of info! I can see the IP address, but this looks private!
>
> * This IP address is only accessible by Kubernetes.

21. Let's create a deployment file called `pico mini-hi-deployment.yaml`. The file includes everything we need to deploy three replicas of our app called `minihi`; that is the name of our app! We will reuse this in a while, so make sure you remember this name.

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mini-hi-deployment
  labels:
    app: minihi 
spec:
  replicas: 3
  selector:
    matchLabels:
      app: minihi
  template:
    metadata:
      labels:
        app: minihi
    spec:
      containers:
      - name: minihi
        image: steliosot/mini-hi:1
        imagePullPolicy: Always
        ports:
        - containerPort: 3000
```

> We will use this file to create our new deployment; we don't have to do it manually.
>
> What is a `.yaml` file? YAML is a language for producing configuration files. Depending on whom you ask, YAML stands for *yet another markup language,* or *YAML ain’t markup language* (a recursive acronym), which emphasises that YAML is for data, not documents. [[What is YAML?](https://www.redhat.com/en/topics/automation/what-is-yaml)]

22. Before we proceed, let's `delete` our current pod, called `mini-hi-pod`.

```bash
$ kubectl delete pods mini-hi-pod
```

23. Ok, we are ready to `apply` our deployment plan!

```bash
$ kubectl apply -f mini-hi-deployment.yaml
```

24. Let's `get` our pods!

```bash
$ kubectl get pods
NAME                                 READY   STATUS    RESTARTS   AGE
mini-hi-deployment-dd4795d74-5zbzt   1/1     Running   0          8s
mini-hi-deployment-dd4795d74-9hc4v   1/1     Running   0          8s
mini-hi-deployment-dd4795d74-pbk8n   1/1     Running   0          8s
```

> :heart:

25. Cool, but... 3 is not enough! I need **ten** more, so `replicas:10`! Let's edit the `mini-hi-deployments.yaml` and replace `replicas:3` with `replicas:10`.

* Let's apply the new configuration.

```
$ kubectl apply -f mini-hi-deployment.yaml
```

26. Let's get the pods.

```bash
$ kubectl get pods
NAME                                 READY   STATUS    RESTARTS   AGE
mini-hi-deployment-dd4795d74-5zbzt   1/1     Running   0          2m49s
mini-hi-deployment-dd4795d74-9hc4v   1/1     Running   0          2m49s
mini-hi-deployment-dd4795d74-bddfb   1/1     Running   0          4s
mini-hi-deployment-dd4795d74-h6g7h   1/1     Running   0          4s
mini-hi-deployment-dd4795d74-k5k75   1/1     Running   0          4s
mini-hi-deployment-dd4795d74-mdhrn   1/1     Running   0          4s
mini-hi-deployment-dd4795d74-pbk8n   1/1     Running   0          2m49s
mini-hi-deployment-dd4795d74-psc85   1/1     Running   0          4s
mini-hi-deployment-dd4795d74-rcvgc   1/1     Running   0          5s
mini-hi-deployment-dd4795d74-wzxcn   1/1     Running   0          4s
```

> :+1: That was easy!

27. Try the `get pods`  using the `wide` option; you can see how pods' have been placed into nodes.

```bash
$ kubectl get pods -o wide

NAME                                 READY   STATUS    RESTARTS   AGE     IP            NODE                                               NOMINATED NODE   READINESS GATES
mini-hi-deployment-dd4795d74-5zbzt   1/1     Running   0          5m16s   10.104.2.8    gke-stelios-cluster13-default-pool-ad4c0a49-c411   <none>           <none>
mini-hi-deployment-dd4795d74-9hc4v   1/1     Running   0          5m16s   10.104.0.6    gke-stelios-cluster13-default-pool-ad4c0a49-27sf   <none>           <none>
mini-hi-deployment-dd4795d74-bddfb   1/1     Running   0          2m31s   10.104.2.10   gke-stelios-cluster13-default-pool-ad4c0a49-c411   <none>           <none>
mini-hi-deployment-dd4795d74-h6g7h   1/1     Running   0          2m31s   10.104.1.5    gke-stelios-cluster13-default-pool-ad4c0a49-rfg7   <none>           <none>
mini-hi-deployment-dd4795d74-k5k75   1/1     Running   0          2m31s   10.104.0.8    gke-stelios-cluster13-default-pool-ad4c0a49-27sf   <none>           <none>
mini-hi-deployment-dd4795d74-mdhrn   1/1     Running   0          2m31s   10.104.1.6    gke-stelios-cluster13-default-pool-ad4c0a49-rfg7   <none>           <none>
mini-hi-deployment-dd4795d74-pbk8n   1/1     Running   0          5m16s   10.104.1.4    gke-stelios-cluster13-default-pool-ad4c0a49-rfg7   <none>           <none>
mini-hi-deployment-dd4795d74-psc85   1/1     Running   0          2m31s   10.104.0.7    gke-stelios-cluster13-default-pool-ad4c0a49-27sf   <none>           <none>
mini-hi-deployment-dd4795d74-rcvgc   1/1     Running   0          2m32s   10.104.2.9    gke-stelios-cluster13-default-pool-ad4c0a49-c411   <none>           <none>
mini-hi-deployment-dd4795d74-wzxcn   1/1     Running   0          2m31s   10.104.2.11   gke-stelios-cluster13-default-pool-ad4c0a49-c411   <none>           <none>
```

> In my case, pods are placed as follows
>
> * Node `gke-stelios-cluster13-default-pool-ad4c0a49-c411` has 4 pods
> * Node `gke-stelios-cluster13-default-pool-ad4c0a49-27sf` has 3 pods
> * Node `gke-stelios-cluster13-default-pool-ad4c0a49-rfg7` has 3 pods

28. Let's deploy a load balancer to help us distribute HTTP traffic (aka `service`). Create a `service` file called `mini-hi-service.yaml`

```
apiVersion: v1
kind: Service
metadata:
  name: mini-hi-service
  labels:
    app: mini-hi-service
spec:
  type: LoadBalancer
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: 3000
  selector:
    app: minihi
  sessionAffinity: None
```

> Note that our selector app is `minihi; that's the same label we used in the previous file.
>
> We also map port 80 (of our Kubernetes cluster) with port 3000 (of our app that is running inside Docker)

29. Ok, let's go for it and `apply` the service.

```bash
$ kubectl apply -f mini-hi-service.yaml
```

> Our `service` load balancer is ready!

30. Let's see the public IP of the load balancer:

```bash
$ kubectl get services
NAME              TYPE           CLUSTER-IP    EXTERNAL-IP    PORT(S)        AGE
kubernetes        ClusterIP      10.108.0.1    <none>         443/TCP        78m
mini-hi-service   LoadBalancer   10.108.8.93   34.133.57.40   80:32326/TCP   6m2s
```

> This is the `EXTERNAL-IP`

31. Go back to your browser and give it a go! Your app is now deployed in a production environment in Kubernetes!

32. Let's see some further info on `services`.

```bash
$ kubectl describe services
```

33. :weary: **Omg! I need to update my software! What should I do?**

* No problem :happy:
* Go on and update your Hello World message.
* Create a new image and then push it to Docker Hub (steps 1 to 6).

* I already created the second version of my software stored in an image called `steliosot/mini-hi:2`
* Let's adapt the `mini-hi-deployment` file.

```
kubectl edit deployment mini-hi-deployment
```

34. Now you need to be careful! Press  `a` (now you are in `-- INSERT --` mode), then move downwards and update the following:

* `replicas: 15`
* `image: steliosot/mini-hi:2`

> **I want 15 replicas!** Make sure you update the `image` to the new image.
>
> To exit, try the next:
>
> * Press `ESC`
> * Type `wq!`
>   * `w` for write
>   * `q` for quit
>   * `!` save and exit!
> * Press `enter`
>
> Welcome to the `vi` world [[What is the VI editor?](https://www.guru99.com/the-vi-editor.html)]
>
> **This command updates the running containers, so we don't need to redeploy; only edit the deployments configuration file and save it!** 

35. Let's see the running pods!

```bash
kubectl get pods
NAME                                  READY   STATUS        RESTARTS   AGE
mini-hi-deployment-586f77d79-4rmjf    1/1     Terminating   0          18m
mini-hi-deployment-586f77d79-6gxnq    1/1     Terminating   0          26s
mini-hi-deployment-586f77d79-9f58z    1/1     Terminating   0          18m
mini-hi-deployment-586f77d79-fbfjd    1/1     Terminating   0          25s
mini-hi-deployment-586f77d79-g5rqn    1/1     Terminating   0          18m
mini-hi-deployment-586f77d79-j5hrc    1/1     Terminating   0          18m
mini-hi-deployment-586f77d79-jjjlb    1/1     Terminating   0          18m
mini-hi-deployment-586f77d79-ltkh7    1/1     Terminating   0          18m
mini-hi-deployment-586f77d79-ltkh7    1/1     Terminating   0          18m
mini-hi-deployment-586f77d79-mdw9h    1/1     Terminating   0          18m
mini-hi-deployment-586f77d79-qrckr    1/1     Terminating   0          18m
mini-hi-deployment-586f77d79-rlpwr    1/1     Terminating   0          18m
mini-hi-deployment-586f77d79-vpmxk    1/1     Terminating   0          18m
mini-hi-deployment-6bf9475958-95h2h   1/1     Running       0          21s
mini-hi-deployment-6bf9475958-fh45g   1/1     Running       0          20s
mini-hi-deployment-6bf9475958-fkn5z   1/1     Running       0          26s
mini-hi-deployment-6bf9475958-n4wpg   1/1     Running       0          25s
mini-hi-deployment-6bf9475958-pq9c5   1/1     Running       0          25s
mini-hi-deployment-6bf9475958-qb5tc   1/1     Running       0          25s
mini-hi-deployment-6bf9475958-qdclf   1/1     Running       0          19s
mini-hi-deployment-6bf9475958-qqj6s   1/1     Running       0          25s
mini-hi-deployment-6bf9475958-t7xd8   1/1     Running       0          19s
mini-hi-deployment-6bf9475958-tnlp6   1/1     Running       0          25s
mini-hi-deployment-6bf9475958-tz6jd   1/1     Running       0          21s
mini-hi-deployment-6bf9475958-tzd8q   1/1     Running       0          21s
mini-hi-deployment-6bf9475958-wd942   1/1     Running       0          20s
mini-hi-deployment-6bf9475958-x6cxv   1/1     Running       0          20s
mini-hi-deployment-6bf9475958-z92tl   1/1     Running       0          25s
```

> :tada: 15 nodes are now up and running!
>
> You might see some pods in `STATUS` `Terminating` , these will be removed after a while... so run this command once more.

36. The final step, go back to your browser and refresh your webpage! Your new updated software is there!

37. Well done! :checkered_flag: You deployed a Kubernetes app using Docker. 

38. Kubernetes is expensive! Don't forget to delete your cluster!
