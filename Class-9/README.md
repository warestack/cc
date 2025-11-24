## Lab9: Introduction to Apache Cassandra

### What am I about to learn?

Today’s lab session focuses on Apache Cassandra. You will install it, run it, and learn the basic commands needed to containerise and deploy a small Cassandra NoSQL cluster.

Lab 9 focuses on how to:

* Configure Cassandra containers on GCP VMs.
* Deploy and run a Cassandra cluster.
* Use basic Cassandra CLI commands to explore and manage data.
* Interact with Cassandra using Python and Node.js

### Phase 1: Setting up our environment

2. To run this tutorial, you will need a **a GCP VM with the Ubutnu as in the previous labs, but make sure it has at least 8 GB of RAM and 30 GB of disk space.** (e.g., an `e2-standard-2`). This is required because we will be running multiple Cassandra containers on the same VM.

2. Start a new terminal session on your VM and run the following commands. 
   **Make sure you understand each command, do not just copy and paste.**
3.  Update the system:

```bash
sudo apt-get update
```

💡**Notes:**

* sudo apt-get update` downloads the latest package information from all configured sources.` 

* `These sources are usually listed in `/etc/apt/sources.list` and `/etc/apt/sources.list.d/`.

* This step ensures your system knows about updated packages and dependencies.

4. Install Docker. Type `Y` when prompted:

```bash
sudo apt-get install docker.io
```

Docker is now installed on your VM.

We only need to install it once—after that we can run as many containers as we like.

5. Check the Docker version:

```bash
sudo docker --version
```

6. Create a new user called `docker-user`, which we will use to run our containers:

```bash
sudo adduser docker-user
```

Set a password when prompted.

You may press **Enter** for the additional fields and type **Y** at the end.

7. Add the new user to the `sudo` group:

```bash
sudo usermod -aG sudo docker-user
```

Without this, `docker-user` will not be allowed to run `sudo` commands.

8. Allow `docker-user` to run Docker commands without needing `sudo`:

```bash
sudo usermod -aG docker docker-user
```

9. Switch to the new `docker-user`:

```bash
su - docker-user
```

The `-` ensures you switch fully into the user's environment and home directory.

10. Test that Docker works:

```bash
docker
```

You should see a full list of Docker commands and options. This confirms that your setup is ready.

---

### Phase 2: Running a Cassandra container

1. Our next step is to create a create a Cassandra container. Let's start a new Cassandra node using Docker. 
   We will name the container `my-cassandra-1`:

```bash
docker run --name my-cassandra-1 -m 2g -d cassandra:3.11
```

The `-m 2g` option assigns **2 GB of memory** to this container.

2. We have now created an Apache Cassandra container called `my-cassandra-1`.  Check the active containers by running:

```bash
docker ps -a
```

You should see the container listed as running.

3. Before creating our cluster, let's stop the container:

```bash
docker stop my-cassandra-1 
```

4. Then remove it:

```bash
docker rm my-cassandra-1 
```

---

### Phase 3: Building a three-nodes Cassandra cluster

1. We will now create a cluster of three Cassandra nodes. 

   The first node will be called `cassandra-1`, and for this tutorial we will use Cassandra 3.11.

* We will interact with the cluster using `nodetool`.

* `nodetool` is a command-line tool for managing a Cassandra cluster.

  All Cassandra nodes work together as a single distributed database system.

```bash
docker run --name cassandra-1 -d cassandra:3.11
```

2. Use `docker ps -a` to check if your container is up and running. It is good practice to verify each container after creation. Let’s inspect `cassandra-1`:

```bash
docker inspect cassandra-1
```

3. The output contains all configuration details of your container.  To extract only the IP address, use:

```bash
docker inspect --format='{{ .NetworkSettings.IPAddress }}' cassandra-1
# Example output:
# 172.17.0.2
```

4. There are different ways to configure a Cassandra cluster. The most common approach is to link nodes using IP addresses.  Since all our containers run on the same VM, we can simply use their container names.

   Before proceeding, ensure that `cassandra-1` is running:

```bash
docker ps -a
```

:rotating_light: Container creation may fail for various reasons. 

If that happens, stop it (`docker stop <name>`) and remove it (`docker rm <name>`),  then recreate the container.  

If you want to learn how to create Cassandra clusters across different VMs or servers, check Appendix A.

5. Use `nodetool` in `cassandra-1` to verify that our first node is healthy:

```bash
docker exec -i -t cassandra-1 bash -c 'nodetool status'
```

If you see:

`Error: The node does not have system_traces yet, probably still bootstrapping`

This means the container is still starting up. Wait a few moments.

> Expected output:
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
> The `UN` status means the node is Up and Normal.

6. Now let’s create the second Cassandra node, `cassandra-2`:

```bash
docker run --name cassandra-2 -d --link cassandra-1:cassandra cassandra:3.11
```

The `--link cassandra-1:cassandra` option links `cassandra-2` to `cassandra-1`,  allowing them to form a cluster.

7. Check the cluster status again:

```bash
docker exec -i -t cassandra-1 bash -c 'nodetool status'
```

Sample output:

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
> * `UJ` means Up / Joining — still syncing.  
> * The `?` in `Owns` is normal during bootstrapping.  
> * Wait 1–2 minutes and run the command again.  
>
> After syncing
>
> ```
> UN  172.17.0.3  70.92 KiB  256  100.0%  bff8c5c1-8af3-4eb9-bfce-a6f90c049972  rack1
> UN  172.17.0.2  75.93 KiB  256  100.0%  abc2a2ee-9bff-415f-8cd0-f8a19295e846  rack1
> ```

8. Before creating a third container, check your VM's memory:

```bash
free
```

> Example:
>
> ```bash
>            total        used        free      shared  buff/cache   available
> Mem:        4022808     3368560      117324        1076      536924      436672
> Swap:             0           0           0
> ```
>
> * With 3.36 GB used out of 4 GB, adding another node may fail.  
> * Scale your VM to 8 GB RAM, restart it, and reconnect using:
>
> ```bash
> su - docker-user
> ```
>
> * Run `free` again to confirm available memory.

9. Start the existing containers again:

```bash
docker start cassandra-1 cassandra-2
```

10. Recheck the cluster:

```bash
docker exec -i -t cassandra-1 bash -c 'nodetool status'
```

11. Now add the third Cassandra node:

```bash
docker run --name cassandra-3 -d --link cassandra-1:cassandra cassandra:3.11
```

12. Check all active containers:

```bash
docker ps -a
```

> You should see three running containers:
>
> ```bash
> cassandra-3
> cassandra-2
> cassandra-1
> ```
>
> If any container is `Exited`, delete it and recreate it.

13. Run `nodetool` again (from any node):

```bash
docker exec -i -t cassandra-2 bash -c 'nodetool status'
```

> Now you should see all **three nodes** in the cluster:
>
> ```bash
> UN 172.17.0.3 ...
> UN 172.17.0.2 ...
> UN 172.17.0.4 ...
> ```
>
> * You may need to wait until all nodes reach `UN`.  
> * Cassandra uses a **gossip protocol** for cluster coordination.  
> * You can add more nodes, but remember each container uses CPU/RAM.

13. Great! We now have a fully working 3-node Cassandra cluster running in Docker! 🎉

---

### Phase 4: Using Cassandra's cli `sqlsh` 

1. Now it is time to learn the basic Cassandra commands.

   * We will interact with the cluster using the `cqlsh` command-line interface. This tool allows us to create keyspaces (databases), tables, and insert or query records.
   * We will run the tool inside `cassandra-1`.

   ```bash
   docker exec -it cassandra-1 bash -c 'cqlsh'
   ```

   > After running this command, you are inside the **cqlsh** CLI.  
   >
   > ```cassandra
   > cqlsh>
   > ```

2. Let’s create a database (called a **KEYSPACE** in Cassandra). 

   Our keyspace will be named **music_store**.

   * Run this inside `cqlsh`:

   ```cassandra
   CREATE KEYSPACE music_store
     WITH REPLICATION = { 
       'class' : 'SimpleStrategy', 
       'replication_factor' : 3 
     };
   ```

   > * `SimpleStrategy` is a basic replication strategy used for **single-datacenter** setups.  
   > * `replication_factor = 3` means our data will be copied across all three nodes.

3. Select (USE) the keyspace as the active database:

   ```cassandra
   USE music_store;
   ```

   > You should now see:
   >
   > ```cassandra
   > cqlsh:music_store>
   > ```

4. Let’s create a table and insert some simple data.

   ```cassandra
   CREATE TABLE music_store.music_by_category (
      type text, 
      category text, 
      id UUID, 
      name text, 
      title text,
      PRIMARY KEY (type, id)
   );
   ```

   > * `UUID` generates unique IDs automatically.

5. Insert a record:

   ```cassandra
   INSERT INTO music_store.music_by_category 
    (type, category, id, name, title)
   VALUES
     ('LP record', 'Rock', uuid(), 'Pink Floyd', 'The Dark Side of the Moon');
   ```

6. Select all rows:

   ```cassandra
   SELECT * FROM music_store.music_by_category;
   ```

7. Delete the table:

   ```cassandra
   DROP TABLE music_store.music_by_category;
   ```

8. Now let’s create a table using a more advanced data structure:  a `map<int, text>` (similar to a Python dictionary).

   ```cassandra
   CREATE TABLE music_store.music_by_category (
      type text, 
      category text, 
      id UUID, 
      name text, 
      title map<int,text>,
      PRIMARY KEY (type, id)
   );
   ```

9. Insert a record with a map:

   ```cassandra
   INSERT INTO music_store.music_by_category 
   (type, category, id, name, title) VALUES
   ('LP record', 'Rock', uuid(), 'Pink Floyd', 
     {1975: 'Wish you were here', 1979: 'The Wall'});
   ```

10. Insert another record:

    ```cassandra
    INSERT INTO music_store.music_by_category 
    (type, category, id, name, title) VALUES
    ('LP record', 'Reggae', uuid(), 'Bob Marley', {1984: 'The legend'});
    ```

11. Select all rows:

    ```cassandra
    SELECT * FROM music_store.music_by_category;
    ```

12. To search inside the `title` map, we must create an **index**:

    ```cassandra
    CREATE INDEX ON music_store.music_by_category (title);
    ```

13. Now we can search for records containing a particular value:

    ```cassandra
    SELECT * FROM music_store.music_by_category 
    WHERE title CONTAINS 'The legend';
    ```

14. Exit the `cqlsh` shell:

    ```cassandra
    exit
    ```

    > Want to learn more Cassandra CQL commands? See the official documentation: https://docs.datastax.com/en/cql-oss/3.3/cql/cql_reference/cqlInsert.html

---

### Phase 5: Cassandra and Python

1. Let's create a Python application to connect and extract data!

2. The script will connect to our cluster and select data from a table. To do this, we need the `cassandra-driver`.

3. Install the required packages:

```bash
sudo apt install python3-pip
```

> Type `Y` when prompted.

4. Create a virtual environment and install the Python Cassandra driver:

```bash
# Install venv support
sudo apt install python3-venv python3-full

# Create venv
python3 -m venv venv

# Activate venv
source venv/bin/activate
```

5. Install the Cassandra driver:

```bash
pip install cassandra-driver
```

6. Inspect the IP addresses of the Cassandra containers:

```bash
docker inspect --format='{{ .NetworkSettings.IPAddress }}' cassandra-1 cassandra-2 cassandra-3
```

Example output:

```
172.17.0.2
172.17.0.3
172.17.0.4
```

7. Create a Python file:

```bash
sudo apt install nano
pico test-cassandra.py
```

8. Add the following Python code:

```python
from cassandra.cluster import Cluster 

cluster = Cluster(['172.17.0.2','172.17.0.3','172.17.0.4'], port=9042)
session = cluster.connect('music_store') 
session.set_keyspace('music_store')
session.execute('USE music_store')

rows = session.execute('SELECT * FROM music_store.music_by_category')

for i in rows: 
     print(i)
```

9. Run the script:

```bash
python test-cassandra.py
```

10. Example output:

```
Row(type='LP record', ...)
Row(type='LP record', ...)
```

11. Example query with variables:

```python
search = 'The Wall'
rows = session.execute(
    'SELECT * FROM music_store.music_by_category WHERE title CONTAINS %s', 
    [search]
)
```

12. Stop `cassandra-1` to test cluster replication:

```bash
docker stop cassandra-1
```

13. Run Python script again — data should still be available due to replication.

14. Deactivate the virtual environment:

```bash
deactivate
```

---

### Phase 6: Cassandra and Node.js

1. Create a new directory:

```bash
mkdir node-cassandra
cd node-cassandra
```

2. Install npm:

```bash
sudo apt install npm
```

3. Initialise the project:

```bash
npm init
```

4. Install the Cassandra driver:

```bash
npm install cassandra-driver
```

5. Create the script:

```bash
pico cassandra-app.js
```

6. Add the following Node.js code:

```javascript
let cassandra = require('cassandra-driver');
const keyspace="music_store";
let contactPoints = ['172.17.0.2','172.17.0.3','172.17.0.4'];

let client = new cassandra.Client({
  contactPoints: contactPoints, 
  keyspace:keyspace,
  localDataCenter: 'datacenter1'
});

let query = 'SELECT * FROM music_store.music_by_category'; 
client.execute(query, function(error, result) {
  if(error){
    console.log('Error:', error);
  }else{
    console.log(result.rows);
  }
});
```

7. Run it:

```bash
node cassandra-app.js
```

8. Example output:

```
[ {type: 'LP record', ...}, {type: 'LP record', ...} ]
```

9. Query with parameters:

```javascript
let query = 'SELECT * FROM music_store.music_by_category WHERE title CONTAINS ?'; 
let parameter = ['The Wall'];

client.execute(query, parameter, (error, result)=> {
  if(error){
    console.log('Error:', error);
  }else{
    console.log(result.rows);
  }
});
```

10. Great job — Phase 6 completed!

---

## Appendix

### Cassandra Cluster Across VMs

1. You need **two VMs** with Docker installed.

2. Stop/delete previous Cassandra containers.

3. Open port **7000** in GCP firewall.

4. Get internal VM IPs. Example:
   * VM1 → `<internal-ip-address-vm1>`
   * VM2 → `<internal-ip-address-vm2>`

5. On VM1, run:

```bash
docker run --name cas-c1 -d   -e CASSANDRA_BROADCAST_ADDRESS=<internal-ip-address-vm1>   -p 7000:7000 cassandra:3.11
```

6. Check status:

```bash
docker exec -i -t cas-c1 bash -c 'nodetool status'
```

7. On VM2, run:

```bash
docker run --name cas-c2 -d   -e CASSANDRA_BROADCAST_ADDRESS=<internal-ip-address-vm2>   -e CASSANDRA_SEEDS=<internal-ip-address-vm1>   -p 7000:7000 cassandra:3.11
```

8. Check cluster status on VM1:

```bash
docker exec -i -t cas-c1 bash -c 'nodetool status'
```

9. You now have a Cassandra cluster across two VMs.

10. Apple famously runs 75,000 Cassandra nodes.

11. You can interact with this cluster using any commands from previous phases.

---

### 🔥 How to Open Port 7000 in GCP Firewall

1. Open the VPC network menu, On the left menu: **VPC network → Firewall rules**

2. Click “Create firewall rule”
3. Fill in the firewall rule details.

Use the following values:

| Field               | Value                                                        |
| ------------------- | ------------------------------------------------------------ |
| Name                | `allow-cassandra-7000`                                       |
| Network             | `default` (or your custom network)                           |
| Direction           | Ingress                                                      |
| Action              | Allow                                                        |
| Targets             | All instances in the network (or specify your VMs)           |
| Source filter       | IPv4 range                                                   |
| Source IP ranges    | `0.0.0.0/0` (or restrict to internal IP ranges if preferred) |
| Protocols and ports | Select TCP, enter 7000                                       |

4. Click “Create”. That’s it! The firewall rule is now active.

**💡 Important Notes**

- Port 7000 is used for Cassandra intra-node communication (gossip protocol).

- If your cluster is only internal, use a safer source range such as:

  ```
  10.0.0.0/8
  ```

- Cassandra also commonly uses:

  - 9042 – CQL (client API)
  - 7199 – JMX
  - 7001 – SSL internode communication
