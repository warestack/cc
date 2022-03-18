### Lab9: Introduction to Apache Hadoop MapReduce

#### What am I about to learn?

Today's lab session focused on Apache Hadoop. We will install and run the wordcount applications on Hadoop.

Lab 9focuses on how to:

* Configure a Hadoop container on a GCP VM
* Run a Hadoop job
* Monitor Hadoop environment

You will need to watch the following video on installing and running Hadoop MapReduce on a VM.

> Take your time; make sure you double-check the commands before you run it

1. The following video demonstrates the commands used in this tutorial. 

[![Watch the video](https://i.ytimg.com/vi/MG8S49xbq8M/hqdefault.jpg)](https://youtu.be/MG8S49xbq8M)

> You should run this tutorial on your GCP VM :white_check_mark:

#### Phase 1: Setting up our environment

2. To run this tutorial, you will need a GCP VM. If you don't remember creating a VM, please watch the video. For this tutorial, I used the following configuration.
   * Zone: us-central1-a
   * Machine type: 2 vCPU, 8 GB memory
   * HTTP traffic: On
   * HTTPS traffic: On
   * Image: [ubuntu-1804-bionic-v20220131](https://console.cloud.google.com/compute/imagesDetail/projects/ubuntu-os-cloud/global/images/ubuntu-1804-bionic-v20220131?project=lab-7-270015)
   * Size (GB): 30
3. Open a new terminal connection and run the follow the following commands. Make sure you understand the process. You don't have to memorise the commands.
4. Let's update our system.

```bash
$ sudo apt-get update

Hit:1 http://us-central1.gce.archive.ubuntu.com/ubuntu bionic InRelease
Get:2 http://us-central1.gce.archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]
...
Get:26 http://security.ubuntu.com/ubuntu bionic-security/multiverse Translation-en [4732 B]
Fetched 23.7 MB in 5s (4972 kB/s)                           
Reading package lists... Done
```

>  Note that:
>
>  * The **sudo apt-get update** command downloads package information from all configured sources.
>
>  * The sources often defined in /etc/apt/sources.list file and other files located in /etc/apt/sources.list.d/ directory. 
>
>  * So when you run the update command, it downloads the package information from the Internet. It is helpful to get info on updated packages or their dependencies.

5. We can now install Docker; make sure you type `Y` for Yes when prompted.

```bash
$ sudo apt-get install docker.io

Reading package lists... Done
Building dependency tree       
Reading state information... Done
...
Do you want to continue? [Y/n] Y
...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Processing triggers for ureadahead (0.100.0-21) ...
```

> Docker is now installed on our VM; we can start trying a couple of tasks.
>
> We install docker once (in a VM), then we can use it.

6. What is the Docker version? Run the next command

```bash
$ sudo docker --version

Docker version 20.10.7, build 20.10.7-0ubuntu5~18.04.3
```

7. Let's create a new user called docker-user. You can use this user to run our containers.

```bash
$ sudo adduser docker-user

Adding user `docker-user' ...
Adding new group `docker-user' (1003) ...
Adding new user `docker-user' (1002) with group `docker-user' ...
Creating home directory `/home/docker-user' ...
Copying files from `/etc/skel' ...
Enter new UNIX password: 
Retype new UNIX password: 
passwd: password updated successfully
Changing the user information for docker-user
Enter the new value, or press ENTER for the default
        Full Name []: 
        Room Number []: 
        Work Phone []: 
        Home Phone []: 
        Other []: 
Is the information correct? [Y/n] Y
```

> Make sure you add a password, and you can leave the rest empty—type Y at the end (although you can press enter).

8. We will need to give `sudo` access to our new `docker-user`, so let's add it to the `sudo` group.

```bash
$ sudo usermod -aG sudo docker-user
```

> If we don't add the user in the `sudo` group, we will not run `sudo` commands.

9. Now, run the following command; this will allow us to give `sudo` permissions to docker to run our commands. 

```bash
$ sudo usermod -aG docker docker-user
```

> This command ensures that our new `docker-user` can run docker commands without using the `sudo` keyword. For example, instead of running always: 
>
> ```bash
> $ sudo docker <command> 
> ```
>
> we will be able to run:
>
> ```bash
> $ docker <command>
> ```

10. Let's switch users, type the following command.

```bash
$ su - docker-user
```

> The `-` symbol allows us to switch user (`su`) and change to the target user's home directory.

* We should be ready now! Try the following command to see if everything works fine.

```bash
$ docker
```

* You should be able to see a list of available options and commands. We can always refer to this when we need to explore using commands and options.

#### Phase 2: Running Hadoop

11. We need to open 8088 and 50070RN interfaces) to run the Hadoop containers (default ports of HDFS and YA.
11. Let us pull a Hadoop docker image (version 2.7.0) as follows.

```bash
$ docker pull sequenceiq/hadoop-docker:2.7.0
```

> *  This is an Apache Hadoop 2.7.0 docker image preconfigured with HDFS and YARN to run our jobs.
> * The Hadoop instance includes the code for the MapReduce examples that we will run today (as any Hadoop installation).
> * The image will provide us with an environment to run a simple Big Data job on a Hadoop: Single Node Cluster using Docker. 
> * For the sake of simplicity, we will run just one node today.

12. Let us check the docker images present on your system.

```bash
$ docker images
```

> We should have the sequenceiq/hadoop-docker 2.7.0 image

13. The next step is to create a new Hadoop container using the following command.
    * This command creates a container with 5GB RAM and maps the appropriate services to the VM ports.

```bash
$ docker run -m 5GB -p 8088:8088 -p 50070:50070 -it sequenceiq/hadoop-docker:2.7.0 /etc/bootstrap.sh -bash
```

14. We just deployed a Hadoop ecosystem using Docker (including HDFS and YARN services).
    * We used port 8088 to expose YARN and 50070 to expose HDFS

15. We are now inside the container.

```bash
bash-4.1# 
```

* Let's clear the terminal.

```bash
# clear
```

#### Phase 3: Running a data intensive task on Hadoop

13. In this tutorial we will use the `touch` command to create a text file. [Touch](https://www.geeksforgeeks.org/touch-command-in-linux-with-examples/) allow us to create an empty file (without the need to edit it as with pico e.g. open it and edit). 

    * If you want to learn more about touch run the following command.

    ```bash
    # touch --help
    ```

14. Let us create a new file using touch, note the new `file01` is empty.

```bash
# touch file01
```

15. Let's add some text, we can use the [echo](https://www.geeksforgeeks.org/echo-command-in-linux-with-examples/) command for this task.
    * The `>` symbol takes the output of a command and redirect it into a file (will overwrite the whole file, in our case it is empty). Run the following command.
      * The command will add the given text `can you can a can as a canner can can a can ?` into the `file01`.

```bash
# echo can you can a can as a canner can can a can ? > file01 
```

16. Use the [cat](https://www.geeksforgeeks.org/cat-command-in-linux-with-examples/) command to see the contents of the file.

```bash
# cat file01
```

> This should print `can you can a can as a canner can can a can ?`.

17. Our task is to run a word count program following the MapReduce paradigm to count the word frequencies of the `file01`.

18. Let us create a directory in HDFS. 
    * Remember that Hadoop reads files from the HDFS, and any file added into the HDFS is split into files of a predefined block size (e.g., 64MB or 128MB) depending on the Hadoop configuration. 
    * If the file is less than this size it just occupies the size of the file in the disk and does not allocate the whole block.  
    * Run the following command.

```bash
# /usr/local/hadoop/bin/hdfs dfs -mkdir /user/test/
```

> The commandI will create a folder called `/user/test` in the HDFS.
>
> *  We are using the `hdfs dfs` command that is actually inside the `/usr/local/hadoop/bin/hdfs` directory.

19. Let us create a subdirectory inside the HDFS `/user/test` directory. The new directory is called `input` will include all the input files to our program (e.g. `file01`).

```bash
# /usr/local/hadoop/bin/hdfs dfs -mkdir /user/test/input
```

20. Let us move (`put`)  `file01` in the HDFS.
    * Run the following command to copy `file01` in the HDFS input folder we created in the previous step called  `/user/test/input`.

```bash
# /usr/local/hadoop/bin/hdfs dfs -put file01 /user/test/input
```

21. We are now ready to run the Hadoop MapReduce Wordcount program. The code for this is preinstalled in our container. 
    * Run the following command. 

```bash
# /usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.0.jar wordcount /user/test/input /user/test/output
```

22. Now, let us check the output folder in the HDFS, we can use the `ls` command (as in Linux) in the specific folder.

```bash
# /usr/local/hadoop/bin/hdfs dfs -ls /user/test/output
```

> * Whenever there is a successful creation of a job, the MapReduce runtime creates a `_SUCCESS` file in the output directory.
> * The second file is the output file produced by the reducer of our job.

23. Let us check the output of our file using the cat command.

```bash
# /usr/local/hadoop/bin/hdfs dfs -cat /user/test/output/part-r-00000
```

24. The output of the word count map reduce job looks like this.

```bash
?       1
a       3
as      1
can     6
canner  1
you     1
```

>  We successfully ran a MapReduce job in Hadoop!

21. If you need to run a second job, make sure you create new input and output directories. Alternatively delete the input and  output directories you already created in HDFS. 

    * To delete the input and output directories we can use the following commands.
    * Do not run these commands yet.

    ```bash
    /usr/local/hadoop/bin/hdfs dfs -rm -r /user/test/input
    /usr/local/hadoop/bin/hdfs dfs -rm -r /user/test/output
    ```

22. If we run a program with multiple input files inside the input folder then Hadoop will run the MapReduce phase for all the files. Then it will aggregate the results to one reducer. Let us see an example on how this looks like.

23. Let us add a new `file02`  in the HDSF and run the wordcount once more. First, use `touch` to create a file.

```bash
# touch file02
```

24. Then add the following text.

```bash
# echo Cloud is good Cloud is Scalable Cloud is Fast > file02 
```

25. Then put the file in the HDFS input folder.

```bash
# /usr/local/hadoop/bin/hdfs dfs -put file02 /user/test/input
```

26. Now run the job for all files in input folder. As you can see this command runs the MapReduce program for the wordcount example for all the files inside the `/user/test/input` folder.

```bash
# /usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.0.jar wordcount /user/test/input /user/test/output
```

27. **There is an error!** Let us examine the output... 
    * Did you find the problem?
28. The problem is that **the output folder already exists** in the HDFS! This means that we will need to delete the output folder, so Hadoop will create a new one to add the output of our MapReduce wordcount. Another option is to export the data to a different folder e.g. `/user/test/output-run2`. 
    * In my case I will just delete it using the hdfs `dfs -rm -R` command following by the name of the folder.

```bash
# /usr/local/hadoop/bin/hdfs dfs -rm -R -skipTrash /user/test/output
```

29. Now lets rerun the wordcount job.

```bash
# /usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.0.jar wordcount /user/test/input /user/test/output
```

30. Run the cat command once more to see the output of the reduce phase. 

```bash
# /usr/local/hadoop/bin/hdfs dfs -cat /user/test/output/part-r-00000
```

> The output looks like this:
>
> ```
> ?       1
> Cloud   3
> Fast    1
> Scalable    1
> a       3
> as      1
> can     6
> canner  1
> good    1
> you     1
> ```
>
> * The wordcount was executed for both `file01` and `file02`, since both are in the same input folder.

31.  If you want to run a separate word count for another file, then you will need to create a new input folder.

#### Phase 4: Using Hadoop services to inspect task executions

24. Let us use the Hadoop interface to inspect our Hadoop system

* Enter the URL: **YOUR_IP:50070**
* This is the Hadoop HDFS interface. Take a moment and observe the information in the one node Hadoop cluster.

25. Let us check the DataNodes tab, click on it.
    * We have one DataNode, with all the data about our one node cluster.
26. Finally, let us check the Utilities tab, click on the **Browse the file system**.
    * We can see the HDFS (file system). Click on the user, then test, then output and you will see the output file from our latest Hadoop run.
27. Now, let us access the YARN interface.
    * Visit the URL: **YOUR_IP:8088**
    * The YARN interface shows information about the jobs submitted in the cluster. Take a minute to look around the different options.

#### Phase 5: Running a computational intensive task on Hadoop

24. Let us run a **computationally intensive task** in contrast to the word count that is a **data intensive task** 
    * A computationally intensive task requires extensive CPU and/or memory resources and is usually refers to a scientific problem or calculation. 
    * Our task is to estimate the pi (3.14) value using a Monte Carlo simulation.
    * The algorithm calculates the probability of a point to be inside the area of a circle to estimate the value of pi.
    * This is one of the most common ways to calculate pi! If you want to know more about it read [this](https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/) article. Also, this [link](https://academo.org/demos/estimating-pi-monte-carlo/) provides a nice visualisation demonstration of the algorithm.
25. In our first run we will run **4** mappers, with **100** samples (our data points for the pi estimation using the Monte Carlo simulation) per mapper.

```bash
# /usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.0.jar pi 4 100
```

> The output looks like this:
>
> ```bash
> Number of Maps = 4
> Samples per Map = 100
> ...
> Job Finished in 40.374 seconds
> Estimated value of Pi is 3.17000000000000000000
> ```

26. Our estimation is 3.17 (not so good, not so bad). In my case it took 40.37 seconds to run it.

27. Now let us run the same command (step 51) using **10** mappers, with **100** samples per map. As we can see the pi estimation is now better, yet it requires more the time to complete. 

```bash
Number of Maps = 10
Samples per Map = 100
...
Job Finished in 59.281 seconds
Estimated value of Pi is 3.14800000000000000000
```

28. You can visit the YARN interface on your browser (**YOUR_IP:8088**) and check the job executions.

29. These are the traditional tasks that a Hadoop MapReduce program can run in parallel so our applications can benefit from fast parallel processing. 
    * The same commands will run exactly in a cluster of one node or thousand nodes.

30. :checkered_flag: Well done, you just deployed and ran your first Hadoop MapReduce applications.

>  Want to learn more about Hadoop?
>
> [Hadoop: The Definitive Guide (4th Edition)](http://grut-computing.com/HadoopBook.pdf)