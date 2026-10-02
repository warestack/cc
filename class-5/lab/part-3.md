### Week 5 Part 3: Linux Commands for Cloud Work

In this part, you will practise the Linux commands you need before Docker.

You should already be connected to your `lab-5` VM and switched to your lab user.

#### What You Will Learn

- How to move around the Linux filesystem.
- How to create folders and files.
- How to view file contents.
- How to install software.
- How to remove files and folders safely.

#### Part A: Basic Commands

1. Print your current directory:

```bash
pwd
```

2. List the files and folders in your current directory:

```bash
ls
```

3. List files with detailed information:

```bash
ls -l
```

<details>
<summary>What extra information does `ls -l` show?</summary>

It shows details such as permissions, owner, group, file size, and modification time.

</details>

4. Clear the terminal:

```bash
clear
```

#### Part B: Create Folders and Files

5. Create a folder:

```bash
mkdir cloud-practice
```

6. Move into it:

```bash
cd cloud-practice
```

7. Confirm your location:

```bash
pwd
```

8. Create a text file:

```bash
pico notes.txt
```

Add this text:

```text
I am practising Linux commands on a cloud VM.
```

Save and exit:

- Press `Ctrl + S` to save.
- Press `Ctrl + X` to exit.

9. Print the file contents:

```bash
cat notes.txt
```

10. Move back to your home directory:

```bash
cd
```

<details>
<summary>What command moves directly to your home directory?</summary>

```bash
cd
```

</details>

#### Part C: Install a Small Tool

11. Update the package list:

```bash
sudo apt update
```

12. Install `nano`, which provides the `pico` editor used in this material:

```bash
sudo apt install -y nano
```

#### Part D: Copy and Remove

13. Copy the practice folder:

```bash
cp -r cloud-practice cloud-practice-backup
```

14. Check both folders exist:

```bash
ls
```

15. Remove the backup:

```bash
rm -r cloud-practice-backup
```

> [!WARNING]
>
> Be careful with `rm`. It deletes files and folders. Always check the path before running a delete command.

> **Quick question**
>
> Small research task: search the web for how to list only files ending in `.txt` in Linux. What command could you run inside `cloud-practice`?
>
> <details>
> <summary>Show answer</summary>
>
> ```bash
> ls *.txt
> ```
>
> The `*` symbol is a wildcard. It means "match any text before `.txt`".
>
> </details>

Part 3 is complete. Continue to [Homework 1](../homework/homework-1.md).
