### Week 5 Homework 1: VM and Linux Exercise

In this exercise, you will practise the cloud and Linux setup again.

Use Part 1, Part 2, and Part 3 if you struggle.

#### Task A: Create a Practice VM

1. Create a new Ubuntu VM in GCP.

Use these settings:

| Setting | Value |
| --- | --- |
| Name | `lab-5-exercise` |
| Region | Same region as your `lab-5` VM |
| Zone | Any |
| Machine type | `e2-medium` |
| Operating system | Ubuntu |
| Boot disk size | 10 GB |
| Firewall | Allow HTTP traffic and Allow HTTPS traffic |

2. Connect to the new VM using SSH.

3. Run:

```bash
whoami
```

#### Task B: Create a Sudo User

4. Create a new user called `case`:

```bash
sudo adduser case
```

5. Make `case` a sudo user:

```bash
sudo usermod -aG sudo case
```

6. Switch to `case`:

```bash
su - case
```

7. Check the current user:

```bash
whoami
```

You should see:

```text
case
```

8. Check the current directory:

```bash
pwd
```

You should see:

```text
/home/case
```

9. Check that `case` can run administrator commands:

```bash
sudo whoami
```

You should see:

```text
root
```

#### Task C: Practise Files

10. Create a folder called `deployment-notes`.

11. Create a file inside it called `docker-plan.txt`.

12. Add two short lines explaining what you think Docker is used for.

13. Print the file contents in the terminal.

14. List only `.txt` files inside the folder.

#### Task D: Cleanup

15. Delete the exercise VM.

Go to **Compute Engine > VM instances**, select `lab-5-exercise`, and delete it.

16. Stop the main VM.

Go back to the GCP dashboard, open **Compute Engine > VM instances**, select `lab-5`, and click **Stop**.

You can switch this VM on again when you need it for Week 6.

> [!WARNING]
>
> Do not leave cloud resources running when you are not using them. Running resources can spend your coupon credit.

#### Checklist

Before you finish, make sure:

- `case` exists on the exercise VM
- `case` is a sudo user
- `whoami` shows the expected user
- `sudo whoami` returns `root`
- you created and read a `.txt` file
- the exercise VM is deleted
- the main `lab-5` VM is stopped

Homework 1 is complete. Continue to [Homework 2](homework-2.md).
