### Lab10: Introduction to Apache Spark

#### What am I about to learn?

Today's lab session focused on Apache Spark. We will install and run Python applications on Spark.

Lab 9focuses on how to:

* Configure a Spark container on a GCP VM using Dockerfiles
* Run Spark jobs
* Monitor Spark environment

You will need to watch the following video on installing and running Spark on a VM.

> Take your time; make sure you double-check the commands before you run it

1. The following video demonstrates the commands used in this tutorial. 

[![Watch the video](https://i.ytimg.com/vi/C1tmQzHKBC4/hqdefault.jpg)](https://youtu.be/C1tmQzHKBC4)

> You should run this tutorial on your GCP VM :white_check_mark:

#### Phase 1: Setting up our environment

2. To run this tutorial, you will need a GCP VM. If you don't remember creating a VM, please watch the video. For this tutorial, I used the following configuration.
   * Zone: us-central1-a
   * Machine type: 2 vCPU, 8 GB memory
   * HTTP traffic: On
   * HTTPS traffic: On
   * Image: [ubuntu-1804-bionic-v20220131](https://console.cloud.google.com/compute/imagesDetail/projects/ubuntu-os-cloud/global/images/ubuntu-1804-bionic-v20220131?project=lab-7-270015)
   * Size (GB): 50
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

#### Phase 2: Running Spark tasks

11. For this example, we need to open ports: 8080, 8081 and 8082 
12. First, let us pull a Spark container.

```bash
$ docker pull mjhea0/spark:2.4.1
```

13. Let us check the docker images present on your system.

```bash
$ docker images
```

14. The next step is to configure the environment variable in the IP of our VM. Do not worry for the moment about this command; we will discuss it in a while. 

```bash
$ export EXTERNAL_IP=<YOUR_EXTERNAL_IP_ADDRESS>
```

15. Let's clone the Spark repo with the sample scripts.

```bash
$ git clone https://github.com/steliosot/spark-tutorial.git
```

> Let's enter in the `spark-tutorial` folder
>
> ```bash
> $ cd spark-tutorial
> ```

16. Create a copy of the **docker-compose-ONE-WORKER.yml** file, as `docker-compose` file.

```bash
$ cp docker-compose-ONE-WORKER.yml docker-compose.yml
```

>  Now, let us examine the `docker-compose.yml` file. 
>
> We will firstly use this file to run a master-worker setup.

```dockerfile
version: '3.3'
services:
  master:
    image: mjhea0/spark:2.4.1
    command: bin/spark-class org.apache.spark.deploy.master.Master -h master
    hostname: master
    environment:
      MASTER: spark://master:7077
      SPARK_CONF_DIR: /conf
      SPARK_PUBLIC_DNS: ${EXTERNAL_IP}
    expose:
      - 7077
      - 6066
    ports:
      - 4040:4040
      - 6066:6066
      - 7077:7077
      - 8080:8080
  worker1:
    image: mjhea0/spark:2.4.1
    command: bin/spark-class org.apache.spark.deploy.worker.Worker spark://master:7077
    hostname: worker1
    environment:
      SPARK_CONF_DIR: /conf
      SPARK_WORKER_CORES: 2
      SPARK_WORKER_MEMORY: 1g
      SPARK_WORKER_PORT: 8881
      SPARK_WORKER_WEBUI_PORT: 8081
      SPARK_PUBLIC_DNS: ${EXTERNAL_IP}
    depends_on:
      - master
    expose:
      - 8881
    ports:
      - 8081:8081
```

17. Let's install the docker-compose utility.

```bash
$ sudo apt install docker-compose
```

18. Then, run the following command to create your Spark cluster.

```bash
$ docker-compose up -d
```

19. Our cluster is ready! We have a Spark master and one worker up and running. Next step let us visit the Spark web interface and examine it.
    * Go on and visit the URL:8080 in your browser, then examine for a minute the interface.
20. We have a working Spark cluster! Now let us run a simple example using the `count.py` file. 

```python
try:
    from pyspark import SparkContext, SparkConf 
    from operator import add
except Exception as e:
    print(e)
def get_counts():
    # That is my example of word counting
    words = "can you can a can as a canner can can a can" 
    # Create a new word count application
    conf = SparkConf().setAppName('word count')
    # Start a new context
    sc = SparkContext(conf=conf)
    # split the words in a list
    seq = words.split()
    # parallelize the list of data
    data = sc.parallelize(seq)
    # Run the count on Spark
    counts = data.map(lambda word: (word, 1)).reduceByKey(add).collect()
    # Stop the count
    sc.stop()
    # Print the results!
    print('\n{0}\n'.format(dict(counts)))
if __name__ == "__main__":
    get_counts()

```

21. To run the job on spark, we will need to copy the file in the Spark master, then start a job on it.
    * Run the following command to export the container id of the master node, so we do not have to locate it manually and copy and paste it each time we need it.

```bash
$ export CONTAINER_ID=$(docker ps --filter name=master --format "{{.ID}}")
```

22. Next, copy `count.py` in the master container, inside the `tmp` directory.

```bash
$ docker cp count.py $CONTAINER_ID:/tmp
```

23. Finally, run the Spark job, this is one command to start our job.

```bash
$ docker exec $CONTAINER_ID \
  bin/spark-submit \
    --master spark://master:7077 \
    --class endpoint \
    /tmp/count.py
```

> The job is running! Wait for a minute to complete. 
>
> * At the end you will see the results

24. **We just ran our first word counter on Spark!** Now go back to your Spark web interface and refresh the master site. The app is there as word count. 
25. Now, create a copy of the **docker-compose-EXTRA-WORKER.yml** file, as `docker-compose` file.

> Let's examine this file. As you can see it is exactly the same as the previous compose file, but this one has an extra worker (`worker2`).

```dockerfile
version: '3.3'
services:
  master:
    image: mjhea0/spark:2.4.1
    command: bin/spark-class org.apache.spark.deploy.master.Master -h master
    hostname: master
    environment:
      MASTER: spark://master:7077
      SPARK_CONF_DIR: /conf
      SPARK_PUBLIC_DNS: ${EXTERNAL_IP}
    expose:
      - 7077
      - 6066
    ports:
      - 4040:4040
      - 6066:6066
      - 7077:7077
      - 8080:8080
  worker1:
    image: mjhea0/spark:2.4.1
    command: bin/spark-class org.apache.spark.deploy.worker.Worker spark://master:7077
    hostname: worker1
    environment:
      SPARK_CONF_DIR: /conf
      SPARK_WORKER_CORES: 2
      SPARK_WORKER_MEMORY: 1g
      SPARK_WORKER_PORT: 8881
      SPARK_WORKER_WEBUI_PORT: 8081
      SPARK_PUBLIC_DNS: ${EXTERNAL_IP}
    depends_on:
      - master
    expose:
      - 8881
    ports:
      - 8081:8081
  worker2:
    image: mjhea0/spark:2.4.1
    command: bin/spark-class org.apache.spark.deploy.worker.Worker spark://master:7077
    hostname: worker2
    environment:
      SPARK_CONF_DIR: /conf
      SPARK_WORKER_CORES: 2
      SPARK_WORKER_MEMORY: 1g
      SPARK_WORKER_PORT: 8882
      SPARK_WORKER_WEBUI_PORT: 8082
      SPARK_PUBLIC_DNS: ${EXTERNAL_IP}
    depends_on:
      - master
    expose:
      - 8882
    ports:
      - 8082:8082
```

26. Let's build it!

```bash
$ docker-compose up -d
```

27. Let us refresh our Spark web interface; we should be able to see the node in our worker list. Now we have two workers (worker 1 and worker 2)!
    * Worker 2 is running at port 8082. If we want to have access to the worker interface, we will need to open the port on the GCP. Go on and open the port. Edit the firewall rules and add the 8082, then save it. Go to your browser and click on worker 2; it should be now accessible.

28. Let us run once more the count.py, use the following command.
29. We just ran an application on a Spark cluster of three nodes. The counter spawns two tasks executed in parallel in worker 1 and worker 2. Let us have a look at the master interface. The job is now completed, so its status should be *FINISHED*.
    * As you can observe, we used 4 cores and 1GB memory per executor (each executor has 2 cores).
    * Task execution takes more time in two nodes as our task is tiny; when run in two nodes, we spend more time communicating than running it.
30. Let us write a simple Spark job. The Spark job will include two transformations and one action.
    * As a reminder, a transformation is a process of data filtering and action is applying an operation to the transformations.
    * Spark provides lazy evaluations, so our transformations will not be executed until we trigger an action, in our case, the (count). 
    * Check the `example1.py`.

```python
try:
    # Import all the necessary libraries
    from pyspark import SparkContext, SparkConf
    import random
except Exception as e:
     print(e)
# I define a function to filter numbers to positive numbers
def positive(a):
    if a>0:
       return a
# I define a function to filter numbers to even numbers
def even(a): 
    if a%2==0:
       return a
# I define the runit, where I apply the Spark methods
def runit(x,y):
     # First, create a new Spark application
     conf = SparkConf().setAppName('Example1 application')
     # Then, I define a new Spark context 
     sc = SparkContext(conf=conf)
     # Then, I define my first transformation (filter positive numbers)
     # to a list of random numbers within a range(x,y)
     tr1 = sc.parallelize(range(x, y)).filter(positive)
     # Then, I define my second transformation (filter even numbers)
     tr2 = tr1.filter(even)
     # Then, I run a count action, that is to count the values filtered
     # from transformation 1 and transformation 2
     print("Stelios count:",tr2.count())
if __name__ == "__main__":
    runit(-10,10) # Run it for values between -10 and 10

```

31. Let's move `example1.py` to the `tmp` directory of our container.

```bash
$ docker cp example1.py $CONTAINER_ID:/tmp
```

32. Now, let's run it!

```bash
$ docker exec $CONTAINER_ID bin/spark-submit --master spark://master:7077 --class endpoint /tmp/example1.py
```

33. Let us now run a computationally intensive task: the calculation of pi with Spark, like the Monte Carlo simulation example we ran last week on Hadoop MapReduce. This file is called `example2.py`.

```bash
try:
    from pyspark import SparkContext, SparkConf
    from operator import add
    import random
except Exception as e:
     print(e)
# This is a simple function to calculate the inside points 
# of our monte carlo simulation
def inside(p):
     x, y = random.random(), random.random()
     return x*x + y*y < 1
# The runit will parallelise the execution of our code in the executors
def runit(NUM_SAMPLES):
     conf = SparkConf().setAppName('Example 2 pi')
     sc = SparkContext(conf=conf)
     count = sc.parallelize(range(0, NUM_SAMPLES)).filter(inside).count()
     print("Pi is roughly %f" % (4.0 * count / NUM_SAMPLES))
if __name__ == "__main__":
    runit(100)

```

34. To run `example2.py`, we will need to copy the file in the spark master.

```bash
$ docker cp example2.py $CONTAINER_ID:/tmp
```

35. Then run it!

```bash
$ docker exec $CONTAINER_ID bin/spark-submit --master spark://master:7077 --class endpoint /tmp/example2.py
```

> You can increase the number of samples to have better accuracy on the pi calculation, e.g. runit(100) to runit(1000). In this case, you will need to copy the file back to the spark cluster.

36. Finally, let us run a simple example of Spark SQL. In this example, we will use the `people.json`  as an example in Spark.
    * Let us first check whether the file is in the HDFS. 
    * Let us run the following command; as you can see, there are a lot of files for us there to play around with.

```bash
$ docker exec $CONTAINER_ID hdfs dfs -ls examples/src/main/resources/

Found 10 items
-rw-r--r--   1 root root  130 2019-03-27 03:05 examples/src/main/resources/employees.json
-rw-r--r--   1 root root  240 2019-03-27 03:05 examples/src/main/resources/full_user.avsc
-rw-r--r--   1 root root  5812 2019-03-27 03:05 examples/src/main/resources/kv1.txt
-rw-r--r--   1 root root  49 2019-03-27 03:05 examples/src/main/resources/people.csv
-rw-r--r--   1 root root  73 2019-03-27 03:05 examples/src/main/resources/people.json
-rw-r--r--   1 root root  32 2019-03-27 03:05 examples/src/main/resources/people.txt
-rw-r--r--   1 root root  185 2019-03-27 03:05 examples/src/main/resources/user.avsc
-rw-r--r--   1 root root  334 2019-03-27 03:05 examples/src/main/resources/users.avro
-rw-r--r--   1 root root  547 2019-03-27 03:05 examples/src/main/resources/users.orc
-rw-r--r--   1 root root  615 2019-03-27 03:05 examples/src/main/resources/users.parquet
```

37. Let's use the cat command to see the contents of a file in the terminal.

```bash
$ docker exec $CONTAINER_ID hdfs dfs -cat examples/src/main/resources/people.json

{"name":"Michael"}
{"name":"Andy", "age":30}
{"name":"Justin", "age":19}
```

38. Now, let's examine the `example3.py`. The file includes:
    * Let us create a simple python script to perform the following actions.
    * Load the data from the filesystem (JSON to dataframe). Note that this example loads the data from the local file system of each node and not from the hdfs. Each node has the data available as a copy in their local disk.
    * Show the data in the terminal (data as a dataframe)
    * Transform the data to SQL format.
    * Make an SQL query to the data.
      * SELECT all data FROM table people WHERE the age is greater than 20.
      * This query will be executed in parallel following the Spark concept.

```python
from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .appName("Example3 basic SQL") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
# Load the data
df = spark.read.json("examples/src/main/resources/people.json")
# Displays the content of the DataFrame to stdout (standard output)
df.show()
# Create a new view for the people data 
# This transforms the dataframe to SQL style data, to run SQL queries
df.createOrReplaceTempView("people")
# Run your query on spark
sqlDF = spark.sql("SELECT * FROM people WHERE age>20")
# Show the data
sqlDF.show()
```

39. To run `example3.py`, we will need to copy the file in the spark master.

```bash
$ docker cp example3.py $CONTAINER_ID:/tmp
```

40. Then run it!

```bash
$ docker exec $CONTAINER_ID bin/spark-submit --master spark://master:7077 --class endpoint /tmp/example3.py
```