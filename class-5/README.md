# Week 5 — Google Cloud VMs and Linux

Move from local development to a Linux virtual machine on Google Cloud. Create a VM, connect through SSH, create a user with administrator access, and practise the commands needed for next week's Docker lab.

## Learning route

| Order | Activity | Outcome |
| --- | --- | --- |
| Before class | [Preparation — Credit and Compute Engine](preparation.md) | Request and redeem $50 credit, link billing, and enable the API. |
| 1 | [Part 1 — Create your first VM](lab/part-1.md) | Create and check `lab-5` using the required resources. |
| 2 | [Part 2 — SSH, users, and sudo](lab/part-2.md) | Create `student` once and switch to it whenever you reconnect. |
| 3 | [Part 3 — Linux basics](lab/part-3.md) | Navigate, manage files, install an editor, and edit text. |
| 4 | [Exercise 1 — Create a VM independently](lab/exercise-1.md) | Build a second VM and configure its `case` user. |
| 5 | [Exercise 2 — Files, folders, and pico](lab/exercise-2.md) | Apply your Linux skills, then clean up. |
| 6 | [Research homework — Cloud users and sudo](homework/homework-2.md) | Explain why administrator access needs care. |

Use the [Linux command reference](lab/linux-command-reference.md) during the tutorials and exercises. It includes command purposes, examples, and a few optional next steps.

## Before you start

Complete the [preparation guide](preparation.md) before the lab. The current course deadline to request and redeem a coupon is **21 January 2027**; credit is valid through **21 September 2027**.

You need a Google account for the Cloud Console, your Birkbeck email for the education grant request, and the current coupon retrieval link in the module's Moodle Preparation tile. Request with your Birkbeck address and redeem using your personal Google account, following the module's account guidance.

Record your project ID, VM names, zone, and Linux usernames. Keep passwords private. Use the VM row’s **SSH** button to connect. **Cloud Shell is optional**; Part 2 explains it and the alternative `gcloud compute ssh` route. Run Linux user, package, and file commands **only after SSH connects to the VM**. Cloud Shell is a separate managed environment, not the VM you created.

| VM | Lab user | Purpose | End of session |
| --- | --- | --- | --- |
| `lab-5` | `student` | Guided tutorials and Week 6 | Stop it and keep its disk. |
| `lab-5-exercise` | `case` | Both independent exercises | Delete it and its boot disk. |

Create each Linux lab user **once per VM**. On later connections, switch to the existing account.

> [!WARNING]
> Running VMs spend credit. Stopping stops compute usage charges, but retained disks and other resources can still cost money. Complete the cleanup at the end of Exercise 2.

Screenshots illustrate the workflow; your project ID, IP addresses, and account names will differ. Reused source images are labelled as examples. See the [image inventory](assets/README.md) for their origins.
