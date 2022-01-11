### Lab1.2: Using Linux for user management

#### What am I about to learn?

Today's lab session is essential to have a solid start in this module. Make sure you complete all the tasks before the next class.

Lab 1 part 2 focuses on how to:

**Lab 1.2**    Learn how to use Linux commands to manage users of your VM.

**Lab 1.4**    Develop a simple cloud service :cloud: using Python.

#### Lab 1.2: **User management in Unix (Ubuntu 18.04)**

This tutorial describes the steps to manage users with different security privileges. We will mainly use the `sudo` keyword, representing the system's superuser. We already used the `sudo` in lab 1.2 to run commands (for example, installing software). 

>  The `sudo` (from the “**su**peruser **do**” phrase) represents a group of accounts with special security privileges related to installing/uninstalling software, manipulating folders and files, and making system and application configurations.
>
> _Note that numbering continues from Lab 1.2_

42. Let’s create a new user with a different username; for example, you can use your name. In my case, I will create a new user called `bilbo` from the Shire :evergreen_tree:.
    * Note that we are still logged in as our existing user (with sudo privileges).
    * We will use the `sudo adduser` command followed by the user name, in our case, `bilbo`.
    * Enter a password and then complete the rest (or leave it empty by pressing `Enter`).
      * My password is `myprecious`:exclamation:

```shell
$ sudo adduser bilbo
...
Enter new UNIX password: 
Retype new UNIX password: 
passwd: password updated successfully
...
Changing the user information for username
Enter the new value, or press ENTER for the default
    Full Name []: Bilbo Baggins
    Room Number []: Bag end
    Work Phone []: 
    Home Phone []:
    Other []:
Is the information correct? [Y/n] Y
```

43.  Our new user `bilbo` :raising_hand: is now ready.
    * `bilbo` has a new directory in `/home/bilbo`.
    * But `bilbo` is not a superuser (`sudoer`).
44. To add the new user as `sudo`, we need to use the `usermod` command.

```shell
$ sudo usermod -aG sudo bilbo
```

45. This command adds `bilbo` to the `sudo` group. What does `-a` and `-G` stand for? Simple running the `usermod` command. This shows a list of possible options.

```shell
$ usermod
Usage: usermod [options] LOGIN
Options:
...
-G, --groups GROUPS		new list of supplementary GROUPS
-a, --append			append the user to the
                 			supplemental GROUPS mentioned by 
                  			the -G option without removing 
                            	him/her from other groups
...
```

46. Let’s recap; we have a new user `bilbo` that is also a `sudo` user. 

    > :triangular_flag_on_post: The Linux community usually refers to sudo us**er** as **sudoer**. Respectively, `yoda` and `bilbo` are both **`sudoer`** users.

47. I will switch to the new user account using the following command.

```shell
$ su - bilbo
```

> Note that the dash `–` option helps you to change to the new user while at the same time navigating to `bilbo`’s home directory.

48. You can always exit from `bilbo` and return to your current user by running the `exit` command. For the moment, remain as `bilbo`.
49. Now, let’s change the `bilbo`'s password; we will use the `passwd` command. 

```shell
$ sudo passwd bilbo
[sudo] password for bilbo: # Type in the default password
Enter new UNIX password: 
Retype new UNIX password: 
passwd: password updated successfully
```

> :rotating_light: Your password is again hidden.

50. Let’s create a new user called `frodo`; his password is `sting`. Go on and create a new user.

> You might need to go back :arrow_up: to step 42. 

48. We can see the folders created in the home directory using the following command.

> There might be a few user home directories there, :rotating_light: note that user **`ubuntu`** is a `sudoer,` and it is a default created.

```shell
$ ls /home
... bilbo    frodo   ... ubuntu ...
```

49. I will delete user `frodo` :no_good: ; I will need to run the following command for this action.

```shell
$ sudo userdel frodo
```

50. Let's check once more the folders in the home directory.

```
$ ls /home
... bilbo    frodo   ... ubuntu ...
```

> :rotating_light: Mmm.. deleting a user does not necessarily remove the user's home folder.

51. Let's delete it.

```shell
$ rm -rf /home/frodo
rm: cannot remove '/home/frodo/.bash_logout': Permission denied
rm: cannot remove '/home/frodo/.profile': Permission denied
rm: cannot remove '/home/frodo/.bashrc': Permission denied
```

> :rotating_light: We cannot delete it! Except if we are a `sudo`!
>
> `Permission denied` signifies that the folder belongs to `frodo` and not to `bilbo`.

52. Apparently, we need to be a **`sudoer`** to run such commands to force deletion of the folders belonging to other users. Try the following command.

```
$ sudo rm -rf /home/frodo
```

> Now the folder is gone!

53. Let's validate our assumptions.

```
$ ls /home
... bilbo ... ubuntu ...
```

54. Let’s summarize the commands  that need  `**sudoer**` privileges

    * `sudo` _command_ → Runs a command as a superuser

    * `adduser frodo` → Creates a new user `frodo``
    * ``usermod -aG sudo frodo` → Makes `frodo` a superuser
    * `su - frodo` → Switch between users, by navigating into their home directory
    * `passwd frodo` → Change `frodo`'s password.
    * `userdel frodo` → Deletes `frodo`, but not `frodo`'s home directory

55. The following command changes the user privileges from `sudo` to `non-sudo` user, in other words, it downgrades an account privilege.

```
$ sudo gpasswd -d username sudo
```

Make sure that **you always have access to a superuser account before downgrading or deleting other accounts**.

> :rotating_light: Linux operating system allows you to remove `sudo` access from an account that you are already logged in to. If you have only one `sudo` account and you downgrade its privileges, you will lose superuser access to your system. 
>
> This means that your Linux system is now **`sudo locked`** making your system unusable (you cannot install delete etc. but you can list and manipulate only your files).

:checkered_flag: Well done! You completed parts 1 and 2, now do both one more time :muscle: