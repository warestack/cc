### Week 8 Lab 1: Apache Cassandra with Docker and Python

In this tutorial, you will run Apache Cassandra in Docker and create a small Cassandra cluster.

Cassandra is a distributed NoSQL database. It is designed to store data across multiple nodes so the system can continue working even if one node fails.

You will use the Week 5/6 VM with Docker installed.

#### What You Will Learn

- What Cassandra is.
- What a Cassandra cluster is.
- How to run Cassandra with Docker.
- How to check cluster health with `nodetool`.
- How to use `cqlsh`.
- How to create a keyspace and table.
- How to query Cassandra from Python.

> [!WARNING]
>
> Cassandra can be heavy. Use a VM with at least 8 GB RAM and 30 GB disk space, for example `e2-standard-2`.

#### Part A: Prepare the VM

1. Start your GCP VM.

2. Connect with SSH.

3. Switch to your lab user:

```bash
su - YOUR_LAB_USER
```

4. Check Docker:

```bash
docker --version
```

5. Check available memory:

```bash
free -h
```

If the VM has less than 8 GB RAM, stop it and resize it before continuing.

#### Part B: Run One Cassandra Container

6. Pull and run one Cassandra container:

```bash
docker run --name my-cassandra-1 -m 2g -d cassandra:3.11
```

This command starts one Cassandra node.

- `--name my-cassandra-1` gives the container a name.
- `-m 2g` limits the container to 2 GB RAM.
- `-d` runs it in the background.
- `cassandra:3.11` is the Cassandra image.

7. Check the container:

```bash
docker ps -a
```

8. Stop and remove this test container:

```bash
docker stop my-cassandra-1
docker rm my-cassandra-1
```

#### Part C: Create a Cassandra Cluster

9. Start the first real node:

```bash
docker run --name cassandra-1 -m 2g -d cassandra:3.11
```

10. Wait about one minute, then check its status:

```bash
docker exec -it cassandra-1 bash -c 'nodetool status'
```

If you see a message about bootstrapping, wait and run the command again.

`nodetool status` shows the health of the Cassandra cluster.

- `UN` means Up and Normal.
- `UJ` means Up and Joining.
- A new Cassandra node can take a few minutes to become ready.

11. Start the second node:

```bash
docker run --name cassandra-2 -m 2g -d --link cassandra-1:cassandra cassandra:3.11
```

12. Check the cluster again:

```bash
docker exec -it cassandra-1 bash -c 'nodetool status'
```

Wait until both nodes are visible.

13. Start the third node:

```bash
docker run --name cassandra-3 -m 2g -d --link cassandra-1:cassandra cassandra:3.11
```

14. Check all containers:

```bash
docker ps -a
```

15. Check the cluster from any node:

```bash
docker exec -it cassandra-2 bash -c 'nodetool status'
```

Wait until the three nodes are `UN`.

This cluster is running inside one VM.

- Each container is one Cassandra node.
- The nodes communicate with each other.
- Cassandra uses replication to copy data between nodes.

#### Part D: Use Cassandra with `cqlsh`

16. Open the Cassandra CLI:

```bash
docker exec -it cassandra-1 bash -c 'cqlsh'
```

You should see:

```text
cqlsh>
```

17. Create a keyspace:

```cassandra
CREATE KEYSPACE music_store
  WITH REPLICATION = {
    'class': 'SimpleStrategy',
    'replication_factor': 3
  };
```

A keyspace is similar to a database.

- `SimpleStrategy` is fine for a simple single-datacenter lab.
- `replication_factor: 3` asks Cassandra to keep copies across three nodes.

18. Use the keyspace:

```cassandra
USE music_store;
```

19. Create a table:

```cassandra
CREATE TABLE music_by_category (
  type text,
  category text,
  id UUID,
  artist text,
  title text,
  PRIMARY KEY (type, id)
);
```

This table stores music records.

- `type` is the partition key.
- `id` helps identify each row.
- `UUID` is a unique identifier.
- Cassandra tables should be designed around the queries you need to run.

20. Insert two records:

```cassandra
INSERT INTO music_by_category
  (type, category, id, artist, title)
VALUES
  ('LP record', 'Rock', uuid(), 'Pink Floyd', 'The Dark Side of the Moon');

INSERT INTO music_by_category
  (type, category, id, artist, title)
VALUES
  ('LP record', 'Reggae', uuid(), 'Bob Marley', 'Legend');
```

21. Read the records:

```cassandra
SELECT * FROM music_by_category;
```

22. Query by partition key:

```cassandra
SELECT * FROM music_by_category
WHERE type = 'LP record';
```

23. Exit `cqlsh`:

```cassandra
exit
```

#### Part E: Connect with Python

24. Create a project folder:

```bash
mkdir cassandra-python
cd cassandra-python
```

25. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

26. Install the Cassandra Python driver:

```bash
python -m pip install cassandra-driver
```

27. Get the container IP addresses:

```bash
docker inspect --format='{{ .NetworkSettings.IPAddress }}' cassandra-1 cassandra-2 cassandra-3
```

Example output:

```text
172.17.0.2
172.17.0.3
172.17.0.4
```

28. Create `test_cassandra.py`:

```bash
pico test_cassandra.py
```

29. Add this code.

Replace the IP addresses with your own container IPs:

```python
from cassandra.cluster import Cluster

contact_points = ["172.17.0.2", "172.17.0.3", "172.17.0.4"]

cluster = Cluster(contact_points, port=9042)
session = cluster.connect("music_store")

rows = session.execute("SELECT * FROM music_by_category")

for row in rows:
    print(row.type, row.category, row.artist, row.title)

cluster.shutdown()
```

This script connects Python to Cassandra.

- `contact_points` lists Cassandra nodes.
- `Cluster(...)` creates a connection to the cluster.
- `cluster.connect("music_store")` selects the keyspace.
- `session.execute(...)` runs a CQL query.
- `cluster.shutdown()` closes the connection.

30. Run the script:

```bash
python test_cassandra.py
```

You should see the music records printed.

31. Stop one Cassandra node:

```bash
docker stop cassandra-1
```

32. Run the Python script again:

```bash
python test_cassandra.py
```

The data should still be available because it was replicated across the cluster.

33. Start the stopped node again:

```bash
docker start cassandra-1
```

34. Deactivate the virtual environment:

```bash
deactivate
```

#### Part F: Cleanup

35. Stop the Cassandra containers:

```bash
docker stop cassandra-1 cassandra-2 cassandra-3
```

36. Remove the Cassandra containers:

```bash
docker rm cassandra-1 cassandra-2 cassandra-3
```

37. Check that they are gone:

```bash
docker ps -a
```

38. Stop the VM from the GCP dashboard when you finish.

#### Checklist

Before you finish, make sure:

- Docker works on the VM
- three Cassandra containers were created
- `nodetool status` showed the cluster
- `cqlsh` opened successfully
- the `music_store` keyspace was created
- records were inserted and selected
- Python connected to Cassandra
- the Cassandra containers were stopped and removed
- the VM was stopped

Week 8 is complete.
