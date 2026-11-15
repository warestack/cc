# Week 9 — Apache Cassandra

Run a three-node Apache Cassandra cluster in Docker, query a replicated table with CQL and Python, and see what happens when nodes stop responding.

## Lab route

| Activity | Outcome |
| --- | --- |
| [Prepare the VM](lab/part-1.md#1-prepare-the-vm) | Check Docker, memory and disk on a Compute Engine VM. |
| [Start Cassandra](lab/part-1.md#2-start-the-first-node) | Start a seed node and check that all three nodes eventually report `UN`. |
| [Use CQL](lab/part-1.md#4-create-and-query-a-table) | Create a keyspace, then insert, read, update and delete rows. |
| [Connect with Python](lab/part-1.md#5-query-cassandra-from-python) | Query by partition key using container names on a Docker network. |
| [Test a node failure](lab/part-1.md#6-test-failover-and-recovery) | Compare a read with three, two and one node available. |
| [Clean up](lab/part-1.md#7-clean-up) | Remove the practice containers and network, then stop the VM. |

## Before you start

- Use a GCP Compute Engine VM with Ubuntu 24.04 and Docker. If you need to set up a VM, follow [Week 5](../class-5/README.md) first.
- The lab was verified on an `e2-standard-4` VM with 16 GB memory. Use a boot disk of at least 30 GB.
- Run the lab in the VM's SSH terminal using the lab account that can run Docker.
