# Week 8 — Distributed communication with ZeroMQ

Run small Python programs that exchange messages through ZeroMQ sockets. Use the same Ubuntu VM for all programs so you can see the messages in separate SSH terminals.

## Lab route

| Activity | What you will see |
| --- | --- |
| [Set up Python](lab/part-1.md#1-set-up-the-lab) | A virtual environment with PyZMQ that every terminal can use. |
| [Pair](lab/part-1.md#2-pair--one-peer-to-one-peer) | Two peers exchange five messages in each direction. |
| [Request/Reply](lab/part-1.md#3-requestreply--two-clients-one-server) | Two clients receive one response for each request. |
| [Publish/Subscribe](lab/part-1.md#4-publishsubscribe--filter-topics) | One subscriber receives only the selected topic from two publishers. |
| [Push/Pull](lab/part-1.md#5-pushpull--distribute-work) | Two workers share jobs and a collector adds the results. |
| [Clean up](lab/part-1.md#6-clean-up) | Check for remaining lab processes before stopping the VM. |

Start with [the ZeroMQ lab](lab/part-1.md). Keep your existing Week 5 VM and its disk for later labs.
