

###  Lab 7: CI/CD with Terraform, GCP, GitHub actions and node.js :happy:

#### What am I about to learn?

Today's lab session focused on using CI/CD tools to deploy code on the GCP. We will use:

* Terraform as infrastructure as code tool
* GitHub actions to trigger deployments
* GCP platform as the cloud provider

Our task is to develop a CI/CD workflow to set up a GCP VM and then deploy our software from our computer.

**:rotating_light: This tutorial has a series of configuration steps that you need to follow with extra care! Make sure you take your time and allocate at least 1.5 hours to complete this.**

:stop_sign: When you complete this tutorial, make sure you delete everything (as shown in the last part of the video). If you need to redeploy, you can set up the pipeline once more.

:rotating_light:Make sure you deploy your code on private repos.

The tutorial is organised in two parts:

* **Part 1**: Setting up a deployment plan using GitHub actions. In this part, we will deploy a GCP VM using exclusively terraform and GitHub actions.
* **Part 2**: From my computer to production in less than 10 seconds. In the second part, we will develop a simple Node.js app on our computer, and we will push it to production through GitHub actions. We will see how we can update our software fast and efficient.

You will need to watch the following video to follow the step by step commands.

> **Take your time; make sure you double-check the commands before you run them.**

* The following video demonstrates the commands used in this tutorial. 

[![Watch the video](https://i.ytimg.com/vi/4fC0NvhhZrM/hqdefault.jpg)](https://youtu.be/4fC0NvhhZrM)

> **You should run this tutorial on your GCP VM. :white_check_mark:**

#### Part 1: Setting up a deployment plan using GitHub actions

1. First, we need to create a new GitHub token to help us push code to our private repo.

*   The order of clicks for reaching the token generation page is `Developer settings` > `Personal access Tokens` > `Tokens (classic)` > `Generate new token` > `Generate new token (classic)`. Add a Note and selectg repo and workflow, finally click `Generate token`.

  ![git-token](images/git-token.png)

  > Open a text editor and keep a copy of the GitHub token in a text file; you will probably need to use it multiple times.


2. Create a private GitHub repository
   * I will call it **lab7-terraform**

3. In the new **private repository**:
   * Copy, paste, and save the HTTPS address of your new private repo (found via the <> Code menu) in a text editor (such as Notepad), which should be in the form of `https://github.com/<user-name>/<repo-name>.git`

4. Activate the GCP Cloud Shell, by clicking the shell icon in the top right of the GCP console. We will use a seed repo for this tutorial.

   * We will clone the following public repo in our private repo.
   * This is the private repo that we just created, and it we will host our GCP secrets!

5. Go to the GCP Cloud Shell and run the following command to clone the seed repo.

```bash
git clone https://github.com/steliosot/cc-terraform.git
```

6. Then enter in the folder; our task is to push (by mirroring) the seed repo code to your newly created repo.

```bash
cd cc-terraform
```

* Then run the `mirror` command. 

```bash
git push --mirror https://<user-name>:<token>@<repo>
```

> An example of my command is the next:
>
> ```bash
> git push --mirror https://steliosot:abcdefg12345@github.com/steliosot/test.git
> ```
>

* Now exit from your current folder; we will continue working on your private repo.

```bash
cd ..
```

* 6. Delete the folder of the public repository you originally cloned, so it doesn’t get confused with your new private repo.

```bash
rm lab7-terraform -f -r
```

7. Let's `clone` it, run the next command:

```bash
git clone https://<user-name>:<toke>@<repo>
```

* Then enter in your repo folder:

```bash
cd <your-repo-name>
```

* We are ready; you successfully moved code from my public repo to your private repo.

7. The next task will be to run a set of commands to deploy our infrastructure.
   * Keep running commands in your GCP cloud shell.
8. When you reach this point, follow the detailed steps shown in the video starting at 8:10. You can begin directly from this timestamp using the link: https://youtu.be/4fC0NvhhZrM?t=490

  * Run the following command to authorise access to our service account.

```bash
gcloud auth application-default login   
```
>  What is a service account?
>
>  * A service account is **a special type of Google account intended to represent a non-human user that needs to authenticate and be authorised to access data in Google APIs**. 
>  * Your code will run the commands on your behalf.
>
>  Follow the instructions (by watching the video).
>
>  * Do you want to continue (Y/n)?  **Y**
>  * Then click on the link to get your verification code, copy and paste it and press enter.

9. I organised a set of configurations in the `config.sh` file. Run the following command to make our shell script runnable.

```bash
$ chmod +x config.sh
```

10. Let's run it:
    * You only need to define your project-id.
    * :rotating_light: Make sure your project id is correct! Double-check it before you run this command.

```sh
$ ./config.sh <your-project-id> 
```

> Note: To avoid mistakes when typing or copying your project ID, you can also run the script using the environment variable:
> ```./config.sh $GOOGLE_CLOUD_PROJECT```

> This script creates a bucket (to store data) service account and allows access to various GCP API services, so our code can connect and run commands.
>
> * A bucket called: <your-project-id-**bucket**>
> * A service account called: <your-project-id-**sa**>
> * The project region: us-central1
> * The script generates a key; we will use this key to allow GitHub to connect and run commands.

11. Let's ` cat` the `key.json.

```bash
cat key.json
```

* The key needs to be transformed to base 64 encoding used in GitHub.

> What is Base64?
>
> * **Base64** is a group of [binary-to-text encoding](https://en.wikipedia.org/wiki/Binary-to-text_encoding) schemes that represent [binary data](https://en.wikipedia.org/wiki/Binary_data) (more specifically, a sequence of 8-bit bytes) in sequences of 24 bits that can be represented by four 6-bit Base64 digits.

12. Let's configure access to GitHub, visit the following link and paste the contents of the `key.json`.

When you reach this point, continue by following the detailed steps shown in the video starting at 13:11.
You can jump directly to this timestamp using the link: https://youtu.be/4fC0NvhhZrM?t=791

* [base64encode.org](https://www.base64encode.org/)

> Encode your key to base64 format, copy the key and paste it in GitHub in the actions area.
>
> Your key name should be: **GCP_TF_SA_CREDS_BASE64**
>
> **Watch the video and follow the steps!**

13. Now we will need to adjust the `main.yaml` file and alter the `bucket-id` and the `project-id`. Remember, you cloned my repo, so we need to change these variables to yours!

```bash
pico .github/workflows/main.yaml 
```

* Change the `tf_bucket_name` and the `TF_VAR_project_id` to your bucket name that is of the following format:

  ```
  tf_bucket_name: '<your-project-id>-bucket'
  TF_VAR_project_id: '<your-project-id>'
  ```

  > Add the  **-bucket** after the project id.

* Save and exit.

14. Ok, we are ready! Let's set our GitHub username and password to push code into our repo.

```bash
git config --global user.email <email>
```

15. Then run:

```bash
git config --global user.name <username>
```

16. We are ready; let's add our files.

```bash
git add .
```

17. Then commit with a new message `change workflow`, which refers to step 15, where we set the bucket and project ids.

```bash
git commit -m "change workflow"
```

18. Then `push`! Remember, this is your private repo, so make sure you use your token.

```bash
git push https://<user-name>:<token>@<repo>
```

> * Part 1 is now completed; your VM should be up and running and ready to accept code!
>
> * Let's move to Part 2, where we will ship our code from our local computer to GCP.

--------

#### Part 2: From my computer to production in less than 10 seconds!

19. Let's ship our code to the VM! We will create a new repo to host the new Node.js app
20. First, open your VSC and a terminal. Watch the video and follow the steps.

At this stage, continue by following the detailed steps shown in the video starting at 22:00.
You can jump straight to this point using the link: https://youtu.be/4fC0NvhhZrM?t=1320

21. Clone the following repo into your local computer and open the project in VSC.

> In this step, you must add the required secret to your GitHub repository. This is something you should do now, even though the video shows it later.
> So follow these instructions (the written ones), not the timing in the video.
> 
> What you must do now
> - Go to your GitHub repository.
> - Open Settings → Secrets and variables → Actions → New repository secret.
> - Add the secret exactly as described in the step.
> 
> Important note: The video does not add the secret at this point. It adds it much later, at 30:43 in the video:
https://youtu.be/4fC0NvhhZrM?t=1843

* My second seed repo hosts everything we need to deploy a node.js app in a GCP VM.

```bash
git clone https://github.com/steliosot/cc-terraform-node.git
```

* Create a new repo and make a mirror copy of the repo to your folder, as we did at the beginning of Part 1.

```bash
git push --mirror https://<user-name>:<token>@<repo>
```

* :rotating_light: In your new repo-add your secret in base64 format.
* Encode your key to base64 format, copy the key and paste it in GitHub in the actions area.
* Your key name should be: **GCP_TF_SA_CREDS_BASE64**
* Watch the video and follow the steps!

22. Let's create a new simple node app. This will print a `Hello world! v1` message! 
    * Here `v1` refers to the first version of our software.

```javascript
const express = require('express')
const app = express()

app.get('/', (req,res) => {
    res.send('Hello world! v1')
})

app.listen(3000)
```

23. Update your workflow by adding the GCP project id and the link to your new repo.

* Edit the `.github/workflows/main.yaml` file in VSC.
* We will need to make a few basic configurations and update the `PROJECT_ID` and the `GITHUB_REPO_URL`.

```
PROJECT_ID: <your-gcp-project-id>
GITHUB_REPO_URL: https://github.com/<your-username>/<your-repo-name>.git
```
> Replace the placeholder values with your information.

24. We should be ready! :happy:
25. Let's `add`,`commit` and `push` !

```bash
git add .
```

```bash
git commit -m "add node app"
```

```bash
git push https://<user-name>:<token>@<repo>
```

26. Go to your browser and find your VM IP; your app should be up and running (at port 80).

27. Let's make a minor update; let's update your code (`v1` to `v2`)!

```javascript
const express = require('express')
const app = express()

app.get('/', (req,res) => {
    res.send('Hello world! v2')
})

app.listen(3000)
```

28. Before the workflow can run, you must upload your updated files to GitHub.

Run the following commands in the Cloud Shell or your local terminal inside your project folder:

```bash
git add .
git commit -m "Update workflow with project ID and repo URL"
git push
```

This sends your changes to GitHub so the workflow in your private repo can start running.

:tada: Well done!

> When you finish the lab, you must clean up your Google Cloud Platform resources so you don’t incur any costs.
> Follow the clean-up steps shown in the video starting at 37:26: https://youtu.be/4fC0NvhhZrM?t=2246
>
> You must delete the following:
> - Compute Engine VM instances
> - Firewall rules created during the lab
> - Any service accounts you created
> - Any storage buckets used for Terraform state
> - Any other temporary resources deployed by Terraform

------

#### Appendix

Here you can see the configuration included in the `script.sh`.

```bash
#!/bin/bash

PROJECT_ID=$1
PROJECT_REGION="us-central1"
SERVICE_ACCOUNT_NAME="$PROJECT_ID-sa"
BUCKET_NAME="$PROJECT_ID-bucket"

echo "CREATE BUCKET"
gsutil mb -p $PROJECT_ID -l $PROJECT_REGION gs://$BUCKET_NAME

echo "CREATE SERVICE ACCOUNTS"
gcloud iam service-accounts create $SERVICE_ACCOUNT_NAME --project $PROJECT_ID

SERVICE_ACCOUNT_EMAIL="$SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com"

echo "CREATE A KEY"
gcloud iam service-accounts keys create key.json --iam-account=$SERVICE_ACCOUNT_EMAIL

echo "ENABLE ROLES"
gcloud projects add-iam-policy-binding $PROJECT_ID --member='serviceAccount:'$SERVICE_ACCOUNT_EMAIL --role='roles/storage.admin'
gcloud projects add-iam-policy-binding $PROJECT_ID --member='serviceAccount:'$SERVICE_ACCOUNT_EMAIL --role='roles/compute.admin'
gcloud projects add-iam-policy-binding $PROJECT_ID --member='serviceAccount:'$SERVICE_ACCOUNT_EMAIL --role='roles/storage.objectAdmin'

echo "ENABLE SERVICES"

gcloud services enable cloudresourcemanager.googleapis.com
gcloud services enable iam.googleapis.com
gcloud services enable iap.googleapis.com
gcloud services enable compute.googleapis.com

echo "COMPLETED"
```

> The script uses your `PROJECT_ID` to create a bucket, a service account and a key. Then it enables a set of roles and services so we can run our code remotely.
>
 The code sets the `PROJECT_REGION` to `us-central1`, but you can easily change this to your prefered region [[list of GCP regions](https://cloud.google.com/compute/docs/regions-zones)].

:rotating_light: An alternative way is to run these commands ourselves, here, I run each command one after the other. Note that you don't need to run these commands if you run the `config.sh` file.

We can create a bucket to store the terraform state on GCP. Note that the bucket name must be globally unique. The command is the following:

```bash
gsutil mb -p <project_id> -l <region> gs://<bucket_name>
```

> An example of this command is the following:
>
> ```bash
> gsutil mb -p cloud-class-334108 -l us-central1 gs://cloud-class-334108-bucket
> ```

> Click authorise if prompted.

You can create a new service account for Terraform, add a new KEY, download the generated JSON file with the service account credentials.

```bash
gcloud iam service-accounts create <serviceAccountName> --project <project_id>
```

>  An example looks like this:
>
> ```bash
> gcloud iam service-accounts create terraform-sa --project cloud-class-334108
> ```

Then we can create a key using the following command.

```bash
gcloud iam service-accounts keys create key.json --iam-account=<serviceAccount.email>
```

> This command will create a key in your local directory. 
>
> * You can find your service account email in GCP :arrow_right: Search for service accounts.
> * The service account email is always in the following format:
>   * <serviceAccountName>@<project_id>.iam.gserviceaccount.com
>
> An example looks like this:
>
> ```bash
> gcloud iam service-accounts keys create key.json --iam-account=terraform-sa@cloud-class-334108.iam.gserviceaccount.com
> ```

Then you need to assign the required roles to the new service account

Enable storage services (admin)

```bash
gcloud projects add-iam-policy-binding <project_id> --member='serviceAccount:<serviceAccount.email>' --role='roles/storage.admin'   
```

> An example looks like this:
>
> ```bash
> gcloud projects add-iam-policy-binding cloud-class-334108 --member='serviceAccount:terraform-sa@cloud-class-334108.iam.gserviceaccount.com' --role='roles/storage.admin' 
> ```

Enable storage services (object)

```bash
gcloud projects add-iam-policy-binding <project_id> --member='serviceAccount:<serviceAccount.email>' --role='roles/storage.objectAdmin'
```

An example looks like this:

> ```
> gcloud projects add-iam-policy-binding cloud-class-334108 --member='serviceAccount:terraform-sa@cloud-class-334108.iam.gserviceaccount.com' --role='roles/storage.objectAdmin'  
> ```

Then, enable the storage services (admin)

```bash
gcloud projects add-iam-policy-binding <project_id> --member='serviceAccount:<serviceAccount.email>' --role='roles/compute.admin'
```

>  An example looks like this:
>
> ```bash
> gcloud projects add-iam-policy-binding cloud-class-334108 --member='serviceAccount:terraform-sa@cloud-class-334108.iam.gserviceaccount.com' --role='roles/compute.admin'
> ```

Finally, we need to enable a set of cloud APIs

```bash
gcloud services enable cloudresourcemanager.googleapis.com
```
Enable the iam services

```bash
gcloud services enable iam.googleapis.com
```
Enable the iap services

```bash
gcloud services enable iap.googleapis.com
```

Enable the compute services

```bash
gcloud services enable compute.googleapis.com
```

