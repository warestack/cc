# Week 5 — Linux command reference

[Week 5 overview](../README.md) · [Linux tutorial](part-3.md) · [Exercise 2](exercise-2.md)

Use this reference alongside the guided steps. Run Linux commands **inside your VM**, as `student` on `lab-5` or `case` on `lab-5-exercise`. Use sudo only for administrator tasks. Examples using `notes` and `backups` assume you are in `~/cloud-practice` with the tutorial files and directories present. They are examples to choose from, not a script to run from top to bottom.

## Identity, navigation, and help

| Command | Usage | Example | Short description |
| --- | --- | --- | --- |
| `hostname` | Check which computer you reached | `hostname -s` | Prints the short hostname; expect your VM name. |
| `whoami` | Check your current user | `whoami` | Prints `student` or `case` after switching. |
| `id` | Check user and group membership | `id student` | Shows the account's IDs and groups, including `sudo` when granted. |
| `pwd` | Find your current location | `pwd` | Prints the full directory path. |
| `ls` | List filenames | `ls notes/*.txt` | Lists matching text files; `*` matches part of a name. |
| `ls -l` | Inspect permissions and ownership | `ls -l notes` | Shows file details, including owner and size. |
| `ls -la` | Include hidden files | `ls -la` | Adds entries whose names start with a dot. |
| `cd` | Change directory | `cd ~/cloud-practice` | Enters a directory; `cd ..` goes up, `cd` or `cd ~` goes home. |
| `clear` | Tidy the display | `clear` | Clears the terminal display without deleting files. |
| `--help` | Read an external command's options | `grep --help` | Displays usage; also try `ls --help`. |
| `help` | Read Bash built-in help | `help cd` | Explains a command built into the shell. |
| `man` | Read a manual, if installed | `man ls` | Opens a manual page; press `q` to leave. |
| `exit` | Leave the current shell | `exit` | Leaves the lab-user shell first, then SSH on the next exit. |

## Files, folders, and text

| Command | Usage | Example | Short description |
| --- | --- | --- | --- |
| `mkdir` | Create folders | `mkdir notes backups` | Creates two directories in the current location. |
| `mkdir -p` | Create nested folders | `mkdir -p ~/linux-practice/notes` | Creates missing parents; accepts an existing directory. |
| `touch` | Create an empty file | `touch notes/extra.txt` | Creates a missing file; updates timestamps without clearing existing contents. |
| `echo` | Display a line of text | `echo "Hello Linux"` | Prints text to the terminal. |
| `echo … >` | Write or replace a file | `echo "Hello Linux" > notes/extra.txt` | `>` redirects output and overwrites existing contents. |
| `echo … >>` | Append a line | `echo "Second line" >> notes/extra.txt` | `>>` adds text to the end of the file. |
| `cat` | Read a short file | `cat notes/commands.txt` | Prints the whole file; use grep to select particular lines. |
| `grep` | Find matching lines | `grep "Linux" notes/commands.txt` | Searches file contents, with case-sensitive matching by default. |
| `grep -n` | Show matching line numbers | `grep -n "student" notes/commands.txt` | Adds the line number before each match. |
| `grep -i` | Search regardless of case | `grep -i "linux" notes/commands.txt` | Matches `Linux`, `linux`, and other case combinations. |
| `grep -F` | Search literal text | `grep -F "My lab user" notes/commands.txt` | Treats the search string as text rather than a regular-expression pattern. |
| `pico` | Create or edit text | `pico notes/commands.txt` | Opens the editor after installing nano; save Ctrl+O → Enter, exit Ctrl+X. |
| `cp` | Copy a file | `cp notes/commands.txt backups/commands-copy.txt` | Keeps the original and creates a copy. An existing destination can be overwritten. |
| `cp -r` | Copy a directory and its contents | `cp -r notes notes-copy` | Recursively copies `notes` into a new `notes-copy` directory when that destination does not exist. |
| `mv` | Move or rename | `mv backups/commands-copy.txt backups/commands-backup.txt` | Renames this copy; an existing destination can be overwritten. |
| `rm -i` | Remove a specific file | `rm -i backups/commands-backup.txt` | Requests confirmation; deletion has no recycle bin. Check the target first. |
| `rmdir` | Remove an empty folder | `rmdir backups` | Refuses to remove a directory containing entries. |

## Users, administrator access, and packages

Run account-creation commands once, from the initial SSH account. On the exercise VM replace `student` with `case`. Ordinary file work should not use sudo.

| Command | Usage | Example | Short description |
| --- | --- | --- | --- |
| `sudo` | Run one administrator command | `sudo whoami` | Prints `root` for that command; your shell remains your normal user. |
| `adduser` | Create a Linux user | `sudo adduser student` | Creates the account and home directory and asks for its password. |
| `usermod -aG` | Add a supplementary group | `sudo usermod -aG sudo student` | Grants sudo-group membership while preserving other groups; use a new login shell afterward. |
| `su -` | Switch to an existing user's login shell | `su - student` | Asks for that user's Linux password and enters their home directory. |
| `passwd` | Finish/reset a user's password when needed | `sudo passwd student` | Recovery step for an existing account; asks for a new password twice. |
| `apt update` | Refresh available-package information | `sudo apt update` | Downloads package lists; does not upgrade all packages. |
| `apt install` | Install the package supplying pico | `sudo apt install nano` | Installs nano and its pico command on this Ubuntu setup. |
| `command -v` | Locate an installed command | `command -v pico` | Prints its executable path, or nothing if unavailable. |
| `pico --version` | Verify the editor | `pico --version` | Shows the installed editor version. |

## Optional Cloud Shell commands

These run in **Cloud Shell**, before connecting to the VM. Cloud Shell is optional; the VM row's SSH button is the default route. See [the connection tutorial](part-2.md#optional--connect-through-cloud-shell).

| Command | Usage | Example | Short description |
| --- | --- | --- | --- |
| `gcloud config get-value` | Check the selected CLI project | `gcloud config get-value project` | Prints the project ID used by default. |
| `gcloud compute ssh` | Connect to the VM | `gcloud compute ssh lab-5 --zone=us-central1-a --project=YOUR_PROJECT_ID` | Replace the project placeholder; use `lab-5-exercise` for the exercise VM. |

## A few next steps

Try these on your own practice files after completing the tutorial. They are optional and do not require sudo.

| Command | Usage | Example | Short description |
| --- | --- | --- | --- |
| `head` | Preview the beginning | `head -n 2 notes/commands.txt` | Prints the first two lines. |
| `tail` | Preview the end | `tail -n 2 notes/commands.txt` | Prints the last two lines; useful for longer logs. |
| `wc` | Count lines | `wc -l notes/commands.txt` | Counts newline characters; a final line without a newline is not included. |
| `find` | Search for filenames | `find notes -type f -name '*.txt'` | Finds text files under `notes`, including subdirectories. Quote the pattern so find receives it unchanged. |
| `du` | Check directory space | `du -sh notes` | Summarises space used with readable units. |
| `df` | Check filesystem space | `df -h .` | Shows capacity and free space on the filesystem containing the current directory. |
| Pipe (`\|`) | Feed one command's output to another | `ls -l notes \| grep "commands.txt"` | Filters a listing for display; the pipe connects commands. |

`~` means your home directory, `/` the filesystem root, `.` the current directory, and `..` its parent. Paths and search text are case-sensitive unless an option changes this. Put paths containing spaces in quotes. **Ctrl+C** interrupts a running command; `^` in pico's shortcut bar means Control, not a character to type.
