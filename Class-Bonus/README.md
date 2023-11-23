### Lab8: Introduction to Apache Cassandra

#### What am I about to learn?

Today's lab session focused on Apache Cassandra! We will install and run the basic commands to containerise and create a cluster of Cassandra NoSQL nodes.

Lab 8 focuses on how to:

* Configure Cassandra containers on GCP VMs
* Run a Cassandra cluster
* Run the basic commands to interact with Cassandra
* Use Python and Node.js to interact with Cassandra.

You will need to watch the following video on installing and running Apache Cassandra on a VM.

> Take your time; make sure you double-check the commands before you run it

1. The following video demonstrates the commands used in this tutorial. 

[![Watch the video](https://i.ytimg.com/vi/79JVL6N0kuk/hqdefault.jpg)](https://youtu.be/79JVL6N0kuk)

> You should run this tutorial on your GCP VM :white_check_mark:**

#### Phase 1: Setting up our environment

2. To run this tutorial, you will need a GCP VM. If you don't remember creating a VM, please watch the video. For this tutorial, I used the following configuration.
   * Zone: us-central1-a
   * Machine type: e2-medium
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

#### Phase 2: Running a Cassandra container

11. Our next step is to create a create a Cassandra container.

* Let us run a new Casandra node using Docker, we can name the new container `my-cassandra-1`.

```bash
$ docker run --name my-cassandra-1 -m 2g -d cassandra:3.11
```

> The option `-m 2g` will assign 2GB of memory in this container.

12. We just created an Apache Cassandra container `my-cassandra-1; let us check the active containers running the following command.

```bash
$ docker ps -a
```

> The container is up and running!

* Let's stop the container and create our first cluster.

```bash
$ docker stop my-cassandra-1 
```

* Then delete it.

```bash
$ docker rm my-cassandra-1 
```

#### Phase 3: Building a three-nodes Cassandra cluster

13. We will create a cluster of three Cassandra nodes; the first Cassandra node will be called `cassandra-1`. For this tutorial, we will use Cassandra  3.11.

* We will interact with the cluster using the `nodetool`.
* The `nodetool` utility is a command-line interface for managing a Cassandra cluster. The Cassandra cluster will work as one unique database system to manipulate data.

```bash
$ docker run --name cassandra-1 -d cassandra:3.11
```

> Using the `docker ps -a command`, you can check if your container is up and running.
>
> It is good to check if the container is up and running each time we create one. 

* Let us inspect `cassandra-1`.

```bash
$ docker inspect cassandra-1
```

>  The output shows the configuration parameters of our container; if we want to extract a particular value, we can use the following command.
>
> * The command extracts the `IPAddress` of container `cassandra-1`

```bash
$ docker inspect --format='{{ .NetworkSettings.IPAddress }}' cassandra-1

# The output is the container IP address
# 172.17.0.2
```

14. There are different ways to create a cluster; the most common practice is to set up a cluster configuring the IP addresses of containers or VMs. Since we run everything in the same VM, we can use the container names rather than IPs.
    * Before we proceed, let's make sure that our container is up and running. It should be up and running as we extracted the IP address.

```bash
$ docker ps -a
```

> :rotating_light: In some cases, container creation might fail for many reasons, e.g. something went wrong in docker. In this unlikely case, stop (`docker stop <container-name>`) and delete the container (`docker rm <container-name>`) ; then run it again. 
>
> * If you are want to learn more about setting Cassandra clusters using IP addresses, make sure you complete Appendix A, where you can see how to connect containers running on different VMs or servers.

15. Let's use the `nodetool` command in `cassandra-1` to check if our Cassandra node is up and running.

```bash
$ docker exec -i -t cassandra-1 bash -c 'nodetool status'
```

> * If you see `Error: The node does not have system_traces yet, probably still bootstrapping` , which means that the container is not yet up, Cassandra it is still in the installation process.
> * The output should look like this:
>
> ```bash
> Datacenter: datacenter1
> =======================
> Status=Up/Down
> |/ State=Normal/Leaving/Joining/Moving
> --  Address     Load       Tokens       Owns (effective)  Host ID                               Rack
> UN  172.17.0.2  100.22 KiB  256          100.0%            abc2a2ee-9bff-415f-8cd0-f8a19295e846  rack1
> ```
>
> * The output shows that our container is in `UN` status ( Up and Normal) :happy:

16. Let's connect our second container. Run the following command to create the second Cassandra node `cassandra-2`. 

```bash
$ docker run --name cassandra-2 -d --link cassandra-1:cassandra cassandra:3.11
```

> * We used the `--link cassandra1:cassandra` option to link `cassandra-1` to `cassandra-2`. This will create our cluster.

17. Let us check the status of the containers.

```bash
$ docker exec -i -t cassandra-1 bash -c 'nodetool status' 
```

> * The output is:
>
> ```
> Datacenter: datacenter1
> =======================
> Status=Up/Down
> |/ State=Normal/Leaving/Joining/Moving
> --  Address     Load       Tokens       Owns (effective)  Host ID                               Rack
> UJ  172.17.0.3  30.47 KiB  256          ?                 bff8c5c1-8af3-4eb9-bfce-a6f90c049972  rack1
> UN  172.17.0.2  70.9 KiB   256          100.0%            abc2a2ee-9bff-415f-8cd0-f8a19295e846  rack1
> ```
>
> * If you see a question mark (**?**) in **Owns**, that’s fine!
> * You might notice that the status is `UJ` , which means Up and in Join (not yet in Normal status).
> * Wait for the containers to get synchronised; this will take a minute or two, then rerun the same command; the output should look like this:
>
> ```
> Datacenter: datacenter1
> =======================
> Status=Up/Down
> |/ State=Normal/Leaving/Joining/Moving
> --  Address     Load       Tokens       Owns (effective)  Host ID                               Rack
> UN  172.17.0.3  70.92 KiB  256          100.0%            bff8c5c1-8af3-4eb9-bfce-a6f90c049972  rack1
> UN  172.17.0.2  75.93 KiB  256          100.0%            abc2a2ee-9bff-415f-8cd0-f8a19295e846  rack1
> ```
>
> * Both containers are up and running in normal state (`UN`) as part of the same datacenter.

18. Now let's create the third container! Before we proceed, let's see the resource usage of our VM. Run the `free` command to see the available/used memory.

```bash
$ free
```

> * It seems that we already used a lot of memory for the two first containers!
>
> ```bash
>               total        used        free      shared  buff/cache   available
> Mem:        4022808     3368560      117324        1076      536924      436672
> Swap:             0           0           0
> ```
>
> * We used 3.36GB of a total of 4GB
> * If we create a new container, we might run out of resources, so let's scale! :happy:
> * Stop and edit the VM; let's assign 8GB of space.
> * Start the VM once more, connect (`SSH` and change the user to the `docker-user` using `su - docker-user`.
> * Now, run `free` once more.
>
> ```bash
>               total        used        free      shared  buff/cache   available
> Mem:        8145440      220364     7533836         936      391240     7694936
> Swap:             0           0           0
> ```
>
> * We have 8GB memory now; the amount `used` is dropped since the containers are not running, so let's start both.

19. We can start both containers.

```bash
$ docker start cassandra-1 cassandra-2
```

20. Let's run the `nodetool` command once more.

```bash
$ docker exec -i -t cassandra-1 bash -c 'nodetool status'
```

> * The output shows both containers in `UN` status.
>
> ```bash
> Datacenter: datacenter1
> =======================
> Status=Up/Down
> |/ State=Normal/Leaving/Joining/Moving
> --  Address     Load       Tokens       Owns (effective)  Host ID                            
>    Rack
> UN  172.17.0.3  137.64 KiB  256          100.0%            624f33b5-10b0-4231-b101-a5a2d07d17
> fa  rack1
> UN  172.17.0.2  137.47 KiB  256          100.0%            3bba3a8b-c072-4991-93f7-780b3a0071
> 81  rack1
> ```

21. Let's start the third container

```bash
$ docker run --name cassandra-3 -d --link cassandra-1:cassandra cassandra:3.11
```

* Let's see the active containers.

```bash
$ docker ps -a 
```

> The output shows three running containers :smile:
>
> ```bash
> CONTAINER ID   IMAGE            COMMAND                  CREATED          STATUS         PORT
> S                                         NAMES
> 40c75887c93f   cassandra:3.11   "docker-entrypoint.s…"   2 minutes ago    Up 2 minutes   7000
> -7001/tcp, 7199/tcp, 9042/tcp, 9160/tcp   cassandra-3
> 2fad620a2e2b   cassandra:3.11   "docker-entrypoint.s…"   12 minutes ago   Up 5 minutes   7000
> -7001/tcp, 7199/tcp, 9042/tcp, 9160/tcp   cassandra-2
> ae96e2e67b8e   cassandra:3.11   "docker-entrypoint.s…"   12 minutes ago   Up 5 minutes   7000
> -7001/tcp, 7199/tcp, 9042/tcp, 9160/tcp   cassandra-1
> ```
>
> * If one or more containers are in `exited` then something went wrong... In this case, delete the `exited` container and build your cluster again.

22. Then run the `nodetool` again in `cassandra-2`. Note you can run this command to any node, as this refers to the cluster, rather than the node.

```bash
$ docker exec -i -t cassandra-2 bash -c 'nodetool status'
```

> We should be able to see our cluster:
>
> ```bash
> Datacenter: datacenter1
> =======================
> Status=Up/Down
> |/ State=Normal/Leaving/Joining/Moving
> --  Address     Load       Tokens       Owns (effective)  Host ID                            
>    Rack
> UN  172.17.0.3  113.1 KiB  256          66.1%             624f33b5-10b0-4231-b101-a5a2d07d17f
> a  rack1
> UN  172.17.0.2  137.47 KiB  256          66.8%             3bba3a8b-c072-4991-93f7-780b3a0071
> 81  rack1
> UN  172.17.0.4  30.47 KiB  256          67.1%             ce5d8e84-8f62-44e4-a97e-453e55b7ace
> a  rack1
> ```
>
> * Again, you might need to wait for the status to be `UN`, so dont worry about the `?` in `STATUS`.
> * The gossip protocol runs in all the containers and is responsible for controlling information about our cluster (racks, tokens etc.).
> * You can add more nodes in the cluster by running similar commands. Note, that each Cassandra container allocates an amount of computational resources, so you need to monitor if the container fails or not due to insufficient memory or space.

23. Great! We have a Cassandra cluster up and running! 

#### Phase 4: Using Cassandra's cli `sqlsh` 

24. Now it is time to learn the basic Cassandra commands.

* We will interact with the cluster using the `cqlsh` command line interface (cli). The tool will allow me to run commands to create a database, tables and insert records.
* We will run the tool inside `cassandra-1`.

```bash
$ docker exec -it cassandra-1 bash -c 'cqlsh'
```

> By running this command you are inside the `sqlsh` cli. This might remind you SQL stuff!
>
> ```cassandra
> cqlsh>
> ```

25. Let us create a database (in Cassandra it is called a `KEYSPACE`). My keyspace will be called `music_store`.
    * Run these commands in the `sqlsh`

```cassandra
CREATE KEYSPACE music_store
  WITH REPLICATION = { 
   'class' : 'SimpleStrategy', 
   'replication_factor' : 3 
  };
```

> * We use a `SimpleStrategy` and a replication factor `3`. 
> * SimpleStrategy: It is **a basic replication strategy**. It's used when using a single datacenter. This method is rack unaware. It places replicas on subsequent nodes in a clockwise order.

26. Let's `USE` the keyspace. This will be our active keyspace (aka database)

```cassandra
USE music_store;
```

> * Now, you should be inside the new keystone
>
> ```cassandra
> cqlsh:music_store> 
> ```

27. Let us create a table and insert some data.

```cassandra
CREATE TABLE music_store.music_by_category (
   type text, 
   category text, 
   id UUID, 
   name text, 
   title text,
   PRIMARY KEY (type, id));
```

> * The `UUID` will allow us to generate automatically IDs for our example table.

28. Now, time to add data

```cassandra
INSERT INTO music_store.music_by_category 
 (type, category, id, name, title)
VALUES
  ('LP record', 'Rock', uuid(), 'Pink Floyd', 'The Dark Side of the Moon');
```

29. Let's select data using the `SELECT` command.

```cassandra
SELECT * FROM music_store.music_by_category;
```

30. Delete the table using `DROP TABLE` command (like in SQL)

```cassandra
DROP TABLE music_store.music_by_category;
```

31. Now let us adapt our table and insert data in terms of different data structures e.g., key-value data.
    * We will use the map **<int,text>** to set my key-value data entry (similar to a Python dictionary).

```cassandra
CREATE TABLE music_store.music_by_category (
   type text, 
   category text, 
   id UUID, 
   name text, 
   title map<int,text>,
   PRIMARY KEY (type, id));
```

32. Then run the following commands

* First, insert a record with some key value data {key1:value1, ...}.

```cassandra
INSERT INTO music_store.music_by_category 
 (type, category, id, name, title) VALUES
 ('LP record', 'Rock', uuid(), 'Pink Floyd', 
	{1975: 'Wish you were here', 1979: 'The Wall'});
```

* Then insert another record.

```cassandra
INSERT INTO music_store.music_by_category 
(type, category, id, name, title) VALUES
('LP record', ' Reggae', uuid(), 'Bob Marley', {1984: 'The legend'});
```

33. Select all data

```cassandra
SELECT * FROM music_store.music_by_category; 
```

34.  If we want to search in the `title` field, we will need to create an index. The index will allow us to search inside a key for a particular value. Let us create an index for the title column.

```cassandra
CREATE INDEX ON music_store.music_by_category (title);
```

35. Then, run the following command to search for records with title ‘**The legend**’. This will allow us to search inside our key-value data structure.

```cassandra
SELECT * FROM music_store.music_by_category  WHERE title CONTAINS 'The legend' ;
```

36. That is all for now, exit the cqlsh using the “exit” command.

```cassandra
exit
```

> Want to learn more about Cassandra? Check [this](https://docs.datastax.com/en/cql-oss/3.3/cql/cql_reference/cqlInsert.html).

#### Phase 5: Cassandra and Python

37. Let's create a Python applciation to connect and extract data!
38. The script will connect to our cluster and select  data from a table, for this we will need a `cassandra-driver`.
38. Let's install the required packages.

```bash
$ sudo apt install python3-pip

```

> Type `Y` when prompted.

40. Then we need to install the `cassandra-driver`.

```bash
$ pip install cassandra-driver
```
> If this command does not work, try `pip3` instead.

41. We should be ready, first let us inspect the IP addresses of our cluster as we will need to define our cluster in Python.

```bash
$ docker inspect --format='{{ .NetworkSettings.IPAddress }}' cassandra-1 cassandra-2 cassandra-3
```

> The command will show the  `IP` addresses of the containers
>
> ```bash
> 172.17.0.2
> 172.17.0.3
> 172.17.0.4
> ```

42. Let us create a new python called `test-cassandra.py`.

```bash
$ pico test-cassandra.py
```

43. Then add the following code.

> You might notice that Cassandra does not apply any authentication. By default, Cassandra is configured with AllowAllAuthenticator which performs no authentication checks and therefore requires no credentials. 
>
> * If you want to setup authentication you could follow the next tutorial: [Configuring Authentication (Cassandra)](https://docs.datastax.com/en/cassandra-oss/3.0/cassandra/configuration/secureConfigNativeAuth.html)
> * For the moment, we will procees without authentication, assuming that our Cassandra node is under the GCP VPC.

```python
# Import the driver
from cassandra.cluster import Cluster 

# Create a new cluster
cluster = Cluster() 

# Connect to the cluster's default port
cluster = Cluster(['172.17.0.2','172.17.0.3','172.17.0.4'], port=9042)

# Connect to music_store
session = cluster.connect('music_store') 
session.set_keyspace('music_store')

# Use the preffered keyspace
session.execute('USE music_store') 

# Run a query
rows = session.execute('SELECT * FROM music_store.music_by_category')

# Iterate and show the query response
for i in rows: 
     print(i)
```

44. Let's run it.

```bash
$ python test-cassandra.py
```

> The output should be the two data points from Cassandra
>
> ```bash
> Row(type=u'LP record', id=UUID('a53b00fb-8748-48ea-b6f5-1afcf1f4716e'), category=u' Reggae', 
> name=u'Bob Marley', title=OrderedMapSerializedKey([(1984, u'The legend')]))
> Row(type=u'LP record', id=UUID('ed98a0d9-0fc0-4cb9-a6d7-173e667d0727'), category=u'Rock', nam
> e=u'Pink Floyd', title=OrderedMapSerializedKey([(1975, u'Wish you were here'), (1979, u'The W
> all')]))
> ```

45. If you like, you can adapt your `test-cassandra.py` to pass data to a query using a Python variable, in this case I pass a string.

```python
search = 'The Wall'
rows = session.execute('SELECT * FROM music_store.music_by_category WHERE title CONTAINS %s',[search])
```

> This query should bring only data about `The Wall`.
>
> ```bash
> Row(type=u'LP record', id=UUID('ed98a0d9-0fc0-4cb9-a6d7-173e667d0727'), category=u'Rock', name=u'Pink Floyd', title=OrderedMapSerializedKey([(1975
> , u'Wish you were here'), (1979, u'The Wall')]))
> ```

46. Let's try something... Let's stop `cassandra-1` and then run the python scirpt once more. Even a node is down, we should be able to get our data.

```bash
$ docker stop cassandra-1
```

47. Now run the Python script! I can still access my data, the cluster is still working :happy: ; data is replicated! 

> You can start the container (`docker start cassandra-1`).                                                                                                         

#### Phase 6: Cassandra and Node.js 

48. What about node.js? Let's keep going!

49. We will create a new node.js app to connect and extract data from Cassandra.

50. Firstly, create a new folder.

```bash
$ mkdir node-cassandra
```

51. Then enter in the folder.

```bash
$ cd node-cassandra
```

52. Let's install npm.

```bash
$ sudo apt install npm
```

53. Now initialise the project.

```bash
$ npm init
```

> Press enter...

54. Let's install the cassandra driver for node.js

```bash
$ npm install cassandra-driver
```

> If the command failed, try the next `npm install cassandra-driver@3.5`

55. Let's create a script `cassandra-app.js` to select data.

56. Edit a file using `pico` and then edit as follows.

```javascript
//npm install cassandra-driver
let cassandra = require('cassandra-driver');
const keyspace="music_store";
let contactPoints = ['172.17.0.2','172.17.0.3','172.17.0.4'];
let client = new cassandra.Client({
  contactPoints: contactPoints, 
  keyspace:keyspace,localDataCenter: 
  'datacenter1'
});
let query = 'SELECT * FROM music_store.music_by_category'; 
client.execute(query, function(error, result) {
  if(error!=undefined){
    console.log('Error:', error);
  }else{
    console.log(result.rows);
  }
});
```

57. Save and exit, then run it!

```bash
$ node cassandra-app.js 
```

> The results should look like this:
>
> ```bash
> [ Row {
>     type: 'LP record',
>     id: Uuid: a53b00fb-8748-48ea-b6f5-1afcf1f4716e,
>     category: ' Reggae',
>     name: 'Bob Marley',
>     title: { '1984': 'The legend' } },
>   Row {
>     type: 'LP record',
>     id: Uuid: ed98a0d9-0fc0-4cb9-a6d7-173e667d0727,
>     category: 'Rock',
>     name: 'Pink Floyd',
>     title: { '1975': 'Wish you were here', '1979': 'The Wall' } } ]
> ```
>
> * Break the server (ctrl+C)

58. If you want to pass data into the query, you can use the following script.

```bash
//npm install cassandra-driver
let cassandra = require('cassandra-driver');
const keyspace="music_store";
let contactPoints = ['172.17.0.2','172.17.0.3','172.17.0.4'];
let client = new cassandra.Client({
  contactPoints: contactPoints, 
  keyspace:keyspace,localDataCenter: 
  'datacenter1'
});
let query = 'SELECT * FROM music_store.music_by_category WHERE title CONTAINS ?'; 
let parameter =['The Wall'];
client.execute(query, parameter,(error, result)=> {
  console.log('in');
  if(error!=undefined){
    console.log('Error:', error);
  }else{
    console.log(result.rows);
  }
});
console.log('end');
```

59. :checkered_flag: Well done! You completed lab 8! 

#### Appendix: Cassandra cluster in different VMs

60.  Do you want to explore the configuration of Apache Cassandra in different VMs? 

61. To run this tutorial:

* You will need to have two VMs up and running with Docker installed.

* Make sure you stop and delete all the containers (e.g. cassandra-1 etc.). 
* Open port 7000 in the GCP firewall. 

62. To create a Cassandra cluster, we will need to use the internal IP addresses of the VMs. These are the addresses in the GCP console interface. In my case:
    * **<internal-ip-address-vm1>** is the first VM
    * **<internal-ip-address-vm2>** is the second VM.

63. In the first VM: 
    * Connect and change to your desired user, then run the following command,.
    * Make syre you change the internal IP address.

```bash
$ docker run --name cas-c1 -d -e CASSANDRA_BROADCAST_ADDRESS=<internal-ip-address-vm1> -p 7000:7000 cassandra:3.11
```

64. Wait for a minute for the container to be up and running.

```bash
$ docker exec -i -t cas-c1 bash -c 'nodetool status'
```

65. Then run the following command in the **second VM**, make sure you update the IP addresses.

* The `CASSANDRA_SEEDS` sets the IP address from the first VM.

```bash
$ docker run --name cas-c2 -d -e CASSANDRA_BROADCAST_ADDRESS=<internal-ip-address-vm2> -e CASSANDRA_SEEDS=<internal-ip-address-vm1> -p 7000:7000 cassandra:3.11
```

66. Run the `nodetool`command in the first VM.

```bash
$ docker exec -i -t cas-c1 bash -c 'nodetool status'
```

67. You just deployed a Cassandra cluster using two VMs.

68. Note that you have just 2 nodes! Apple has 75.000 nodes of Cassandra running in their systems (CI/CD could speed up this process...)!

69. :checkered_flag: You can interact with the cluster using the same commands from the previous phases.
