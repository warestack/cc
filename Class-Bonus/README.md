###  Bonus Lab: Messaging in distributed systems using ZeroMQ

#### What am I about to learn?

Today's lab session focused on ZeroMQ. We will use Python to develop the different messaging patterns.

You will need to watch the following video to follow the step by step commands.

> Take your time; make sure you double-check the commands before you run them.

* The following video demonstrates the commands used in this tutorial. 

[![Watch the video](https://i.ytimg.com/vi/MgPqctyXXmI/hqdefault.jpg)](https://youtu.be/MgPqctyXXmI)

> **You should run this tutorial on your GCP VM :white_check_mark:**

1. This tutorial introduces the concepts of sockets in Python3 using ZeroMQ. ZeroMQ is an easy way to develop sockets to allow distributed processes to communicate with each other by sending messages. 
   * In its simplest form, a socket (node) “listens” on a specific IP port, while another socket reaches out to form a connection. Using sockets, we can have on-to-one, one-to-many and many-to-many connection patterns. 

2. The patterns of messaging that we will examine today are the following:

   * **Pair:** Exclusive, one to one communication, where two peers communicate with each other. The communication is bidirectional and there is no specific state stored in the socket. The server listens on a certain port, and the client connects to it.

   <img src="images/pair.png" alt="git-token" style="zoom:50%;" />

   * **Client – Server:** A client connects to one or more servers. This pattern allows REQUEST – RESPONSE mode. A client sends a request “zmq.REQ” and receives a reply. 

   <img src="images/client-server.png" alt="git-token" style="zoom:50%;" />

   * **Publish/Subscribe:** A traditional communication pattern where senders of messages, called publishers, send messages to specific receivers, called subscribers. Messages are published without the knowledge of what or if any subscriber of that knowledge exists. Multiple subscribers subscribe to messages/topics being published by a publisher or one subscriber can connect to multiple publishers.

   <img src="images/ps.png" alt="git-token" style="zoom:50%;" />

   * **Push and Pull sockets (aka Pipelines):** Let you distribute messages to multiple workers, arranged in a pipeline. A Push socket will distribute sent messages to its Pull clients evenly. This is equivalent to producer/consumer model, but the results computed by consumer are not sent upstream but downstream to another pull/consumer socket.

   <img src="images/push-pull.png" alt="git-token" style="zoom:50%;" />

   > :rotating_light: **Note:** Working with Sockets could be tricky, running again and again the same code, using the same port number/same socket, could lead to a connection that “hangs” (the server looks like it is running, but it cannot accept connections). This happens because we did not close and destroy the previous connections correctly. 
   >
   > The most appropriate way to address this is to close the socket and destroy the ZeroMQ context. Refer to try – catch blocks of Phase 2 and Phase 3 for more details. 
   >
   > In this tutorial, you might experience such issues, e.g., running multiple times the same server in the same port. If you face hanging problems, you are advised to kill the Python process, clean the TCP port number, and run the server once more (see step 11). 

###### Phase 1: Pairing a server to a client

3. Let us start by creating a new VM, then we will install Python3. 
   * Keep a copy of the VM internal IP, for this tutorial we will use the internal IP address.
4. Open a new terminal connection and run the following commands (one after the other). The last command installs [ZeroMQ](https://zeromq.org/).

```bash
$ sudo apt update
$ sudo apt install software-properties-common
$ sudo apt install python3.8
$ sudo apt-get -y install python3-pip
$ pip3 install pyzmq
```



> Type: Y when prompted.
>
> Many applications these days consist of components that stretch across networks, so messaging is essential. Today we will use TCP for message transferring.

5. You can access your VM using VSC, or you can run the commands using the SSH and edit files with `pico`, in my case I will use SSH. 

> :rotating_light: Make sure you copy code carefully.

6. We will need to create our first **ZeroMQ server**, the server will allow binding with only one client at a time.

* Create a new file called `pair-server.py`, then enter the following code. 

* The code creates a new socket using the **zmq.PAIR** pattern, then binds the server to a particular IP port (that we already openned in GCP). Note that the server will not stop running until we stop it. 
* Have a look at the comments to understand how this works.
* Make sure that you change the <INTERNAL_VM_ADDRESS>; that is the **internal IP address** of the GCP VM; the client port should be the same with the server.

```python
# import the library
import zmq
import time
# Initialize a new context that is the way to create a socket
context = zmq.Context()
# We will build a PAIR connection
socket = context.socket(zmq.PAIR) # We create a PAIR server
# Do not worry about this for the moment...
socket.setsockopt(zmq.LINGER, 0) 
# Create a new socket and "bind" it in the following address
# Make sure you update the address
socket.bind("tcp://<INTERNAL_VM_ADDRESS>:5555") # IP:PORT
# Keep the socket alive for ever...
while True:
    # Send a text message to the client (send_string)
    socket.send_string("Server message to Client")
    # Receive a message, store it in msg and then print it
    msg = socket.recv()
    print(msg)
    # Sleep for 1 second, so when we run it, we can see the results
    time.sleep(1)
```

7. Do not run the server yet, first let us create the client.

8. Create the client and take a minute to examine the comments. I will call it `pair-client.py`.

> Make sure that you change the <INTERNAL_VM_ADDRESS>; the port should be the same as in the server.

```python
import zmq
import time
# Same as before, initialize a socket
context = zmq.Context()
socket = context.socket(zmq.PAIR) # We create a PAIR server
socket.setsockopt(zmq.LINGER, 0)
# Connect to the IP that we already bind in the server
socket.connect("tcp://<INTERNAL_VM_ADDRESS>:5555")
# A counter will help us control our connection
# For example connect until you send 10 messages, then disconnect...
count = 0
while count<10:
    msg = socket.recv()
    print(msg)
    socket.send_string("Hello from Client")
    socket.send_string("This is a client message to server")
    print("Counter: ",count)
    count+=1
    time.sleep(1)
# Destroy the context socket and then close the connection
context.destroy()
socket.close()
```

9. We will need **two** terminal windows to run the **PAIR** example. We will run the server on one window and the client on the other. Now, run it as follows.

* Run the server

```bash
$ python3 pair-server.py
```

* Run the client

```bash
$ python3 pair-client.py
```

10. Examine the output, we just created a new **PAIR** socket.

* The script will terminate when the client completes its connection. Then stop the server (ctrl + c) and kill it.

11. We will need to clear the TCP connection before we run it again. To do this, use the following command.

```bash
$ sudo fuser -k 5555/tcp # 5555 refers to your port number
```

> :rotating_light: Notes:
>
> *  We can run **only one PAIR at a time**, this mean that we cannot have multiple clients, remember this is a **PAIR**, the first client will lock the socket.
>
> * If we run the server once, and the client twice, the second client will “hang”, this means that the second client it will wait for a new server to connect.
> * If we want to run the pair more than once, we will need to kill the server and clear the TCP connection.
> * **PAIRs** are ideal when a client needs to have exclusive access to a server.
> * We can have multiple servers to multiple clients as PAIRs, but we will need to use different PORT numbers for the connections. 

12. **Each phase is independent of each other, so, stop the server, clear the TCP ports, and move to the next phase.** 

###### Phase 2: Pairing a server to multiple clients

13. Let us create a client-server connection, where multiple clients will connect to a single server. This is the most popular messaging pattern.

* Let’s create a server in the context of **REP-REQ** (reply to a request) pattern. 
* We will call the server `rep-server.py`, using port `5555`.

```python
import zmq
import time
try: # Try to create a new connection
    context = zmq.Context()
    socket = context.socket(zmq.REP) # We create a REP server
    # Here we set a linger period for the socket
    # Linger 0: no waiting period for new messages
    socket.setsockopt(zmq.LINGER, 0)
    socket.bind("tcp://<INTERNAL_VM_ADDRESS>:5555")
    while True: # Wait for next request from client
        message = socket.recv()
        print("Received request: ", message)
        time.sleep (1)  
        socket.send_string("Hi from Server")
except KeyboardInterrupt: # “ctr+c” to break and close the socket!
    context.destroy()
    socket.close()
```

14. Now we will develop two Clients that will be identical in terms of their functionality. 

    * **Client 1** will send a “Client 1 Hello world” request

    * **Client 2** will send a “Client 2 Hello world” request to the server. 
    * Let us create a file called `req-client1.py`, then edit as follows, again make sure you change the <INTERNAL_VM_ADDRESS>.

```python
import zmq
import time
context = zmq.Context()
socket = context.socket(zmq.REQ) # We create a REQ client (REQUEST)
socket.setsockopt(zmq.LINGER, 0)
socket.connect("tcp://<INTERNAL_VM_ADDRESS>:5555")
for request in range (1,10):
    print("Sending request Client 1 ", request,"...")
    socket.send_string("Hello from client 1")
    message = socket.recv()
    print("Received reply ", request, "[", message, "]")
socket.close()
context.destroy()
```

15. Let us create a copy of this client and edit it accordingly. Run the following command to make a new copy.

```bash
$ cp req-client1.py req-client2.py
```

16. Then edit the `req-client2.py` and change `client 1` to `client 2`.

> Let's edit the print and socket messages (lines 8 and 9)

```python
import zmq
import time
context = zmq.Context()
socket = context.socket(zmq.REQ) # We create a REQ client (REQUEST)
socket.setsockopt(zmq.LINGER, 0)
socket.connect("tcp://<INTERNAL_VM_ADDRESS>:5555")
for request in range (1,10):
    print("Sending request Client 2 ", request,"...")
		socket.send_string("Hello from client 2")
    message = socket.recv()
    print("Received reply ", request, "[", message, "]")
socket.close()
context.destroy()
```

17. To run this example, we will need **three** terminal windows, one for the server and two for the clients. Run the following in the first terminal.

* Let's start the server

```bash
$ python3 rep-server.py
```

* Let's start the first client

```bash
$ python3 req-client1.py
```

* Let's start the second client

```bash
$ python3 req-client2.py
```

18. Check the output of the windows, we just created two clients talking to one server. You can have as many clients as you want, you will need to make clients, even with different functionalities that connect to one server.

> :rotating_light: **Notes:**
>
> *  Client – Server is the most widely used pattern, we already used it in class 1 when we installed and ran the Apache HTTP server.
>
> * **Stop the server and clean TCP port 5555** 
>
>   * Kill the server: 
>
>     ```bash
>     $ sudo fuser -k 5555/tcp 
>     ```

###### Phase 3: Pairing a server to a client

19. The publish – subscribe pattern is a very common way to control broadcasting of data to many clients that are subscribed to a context, in a way that servers send data to one or more clients. 

    * To run multiple servers, we need to map each server to a PORT number.

    * In this pattern, messages are published (broadcasted) without knowing that subscribers exist, or if there are any subscribers of this context. 

    * It is the task of the subscribers to make connections and filter out the incoming data.

    * We usually say: Subscribers, subscribe to a specific context.

20. Let us first create a simple example. 

    * We will create two servers that generate weather data, and one client that it is subscribed to both instances to collect data about a particular context:

    * The context is: **Client will only “listen” the context related to New York City weather data (postal code 10001)**.

    * The first instance of our server will run in port `5555`.

      * This instance generates a topic with an ID.

      * For testing purposes, the topic represents a postcode (in our example, that is a random value between 9999 and 10005).
      * Each time a topic is generated the server also generates weather data e.g., temperature, that actual forms our message.

    * The second instance of our server will run in port `5556` and will provide the same functionality.

    * This instance generates similar topics and messages. 

    * **The assumption here is that both instances represent sensors that send weather data from various areas in different cities.**

    * We will create the server code and make it easy to replicate, as you might noticed the only parameter to change is the PORT number.

21. Let us create a new file, call it `pub_server.py`.

    * The server will accept two arguments from the command line, that will be the IP and the PORT value.
      * For accepting command line arguments we use the `sys` Python library.

    * By this way we can run multiple servers, and each time we run the script we will just have to pass IP and PORT number as arguments to the code. For example: 

```bash
$ python3 pub_server.py <internal-ip> <port>
```

* This command will instruct python to run a server in specific <internal-ip> and <port>

```python
import zmq
import random
import sys
import time
try:
    # Port value is the first argument from the command line
    ip = sys.argv[1]
    port = sys.argv[2]
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://"+ip+":"+port) 
    while True:
        # Topic is the post code, randomly generated 9999-10005
        topic = random.randrange(9999,10005)
        # Let us generate the message data (temperature)
        messagedata = random.randrange(1,215)-80
        # Print the data
        print("%d %d" % (topic, messagedata))
        socket.send_string("%d %d %d" % (topic, messagedata, int(port)))
         # Each sensor generates data each second
        time.sleep(1)
except KeyboardInterrupt:
    context.destroy()
    socket.close()
```

22. Create a new file `pub_client.py`. 
    * The script accepts three arguments from the command line (that are the IP and the two ports).

```python
import sys, zmq
try:
    ip = sys.argv[1]
    port1 =  sys.argv[2] # Take port1 from command line
    port2 =  sys.argv[3] # Take port2 from command line
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    print("Collecting updates from weather servers...")
    socket.connect ("tcp://"+ip+":"+port1) 
    socket.connect ("tcp://"+ip+":"+port2)
    topicfilter = "10001"  # Subscribe to postal code e.g. NYC, 10001
    # Subscribe to topicfilter: 10001, WE CARE ONLY FOR NYC!
    socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)
    total_value = 0
    # Lets collect up to 5 subscriptions 
    # Then we will calculate the average of 5 temperatures from NYC
    for update_nbr in range (1,10):
        data = socket.recv()
        topic, messagedata,port = data.split()
        total_value += int(messagedata)
        print("Topic: '%s', message: '%d' on port '%d' "%
              (topic, int(messagedata), int(port)))
        print("Average messagedata value for topic '%s' was %dF" % 
                 (topicfilter, total_value / update_nbr))
except KeyboardInterrupt:
    context.destroy()
    socket.close()
```

23. We are ready to run our **pub-sub** application! We will need **three** terminal windows. In the first terminal run:

```bash
$ python3 pub_server.py <internal-ip> 5555
```

*  In the second terminal run:

```bash
$ python3 pub_server.py <internal-ip> 5556
```

* Each server generates weather data. For example:
  * The postal code, e.g.: 10001
  * The temperate, e.g.: -68

24. Let’s run the client to connect and subscribe to data by postal code e.g., 10001 (NYC). Remember the client script subscribes to both server instances. Run the next command:

```bash
$ python3 pub_client.py <internal-ip> 5555 5556 
```

* When you finish kill the servers (ctrl+z) and clear the TCP ports running the next commands:

  ```bash
  $ sudo fuser -k 5555/tcp
  ```

  ```bash
  $ sudo fuser -k 5556/tcp
  ```

###### Phase 4: Push/Pull: Using a Pipeline pattern**

25. Push/Pull sockets let you distribute messages to multiple workers, arranged in a pipeline. This is very useful for running code in parallel. A Push socket will distribute messages to its Pull clients evenly, and the clients will send a response to another server, called collector.

![git-token](images1/push-pull.png)

* This is equivalent to producer/consumer model, but the results computed by consumer are not sent upstream but downstream to another pull/consumer socket.

* We will implement the following functionality.
* The producer will PUSH random numbers from 0 to 10 to the consumers.
* Two instances of the same consumer will PULL the numbers and will perform a heavy task.
* The task could be any heavy calculation e.g., matrix multiplication.
* For simplicity, our “heavy task” will just return the same number.
* The consumers will PUSH the individual results (heavy task calculations) to a **Result Collector**, that will aggregate the results.
* For simplicity, an instance of the **Result Collector** will PULL the results and calculate the partial sum of each consumer. We can easily sum the two partial sums if needed.
* Let us see a simple example.
  * Producer generates [1,2,3,4,5].
  * Consumer 1 receives [2,4], then calculates a heavy task and forwards results to the Result Collector.
  * Consumer 2 receives [1,3,5], then calculates a heavy task and forwards results to the Result Collector.
  * The result collector calculates the counts and partial sums e.g.:
    * Consumer1[2,4], this means **2** numbers received from Consumer1 and their sum is **6**.
    * Consumer2[1,3,5], that means **3** numbers received from this Consumer2 and their sum is **9**.

* This example demonstrates the potential of distributed processing for parallel processing.

26. Firstly, let us create the producer called `producer.py` running on port `5555` make sure you adapt your <internal-ip>.

```python
import time
import zmq
import random

def producer():
    mysum = 0
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://<internal-ip>:5555") # UPDATE THE IP!
    # Generates 10 numbers
    for num in range(10):
        val = random.randint(1,5) # Random numbers: 1 to 5
        work_message = {'num' : val}
        zmq_socket.send_json(work_message)
        print(work_message)
        mysum = mysum+val
        time.sleep(1)
    return mysum

print(producer())
```

27. Then create the `consumer.py` is as follows. Do not forget to change the two <internal-ip>s in code.

```python
import time
import zmq
import random
def heavyTask(i):
    # Perform a heavy task
    # Here we can perform any heavy calculation e.g. i**100+i*200
    return i # For simplicity we return the same value...
def consumer():
    consumer_id = random.randrange(1,10005)
    print("I am consumer #%s" % (consumer_id))
    context = zmq.Context()
    # receive work from producer (port 5555)
    consumer_receiver = context.socket(zmq.PULL)
    # UPDATE THE IP!
    consumer_receiver.connect("tcp://<internal-ip>:5555")
    # send work to collector (port 5556)
    consumer_sender = context.socket(zmq.PUSH)
    # UPDATE THE IP!
    consumer_sender.connect("tcp://<internal-ip>:5556") 
    while True:
        work = consumer_receiver.recv_json()
        data = work['num']
        result = {'consumer' : consumer_id, 'num' : heavyTask(data)}
        print(result)
        consumer_sender.send_json(result)
consumer() # Run the consumer
```

28. Finally, let us develop the `collector.py`, again change the <internal-ip>.

```python
import zmq
import pprint
context = zmq.Context()
# Pull the results from port 5556 (consumers)
results_receiver = context.socket(zmq.PULL)
results_receiver.bind("tcp://<internal-ip>:5556") # UPDATE THE IP!
collecter_data = {}
data = {}
asum=0
for x in range(10):
   result = results_receiver.recv_json()
   print(result['num'])
   if result['consumer'] in collecter_data:
      # This is how to count and sum items in a dictionary...
      collecter_data[result['consumer']][0] = collecter_data[result['consumer']][0] + 1
      collecter_data[result['consumer']][1] = collecter_data[result['consumer']][1]+result['num']
   else:
      collecter_data[result['consumer']] = [1, result['num']]
pprint.pprint(collecter_data)
```

29. Make sure you don’t have an indentation error!

    * Let us run it and examine how the pipeline works.

    * We will need **four** terminal windows.

30. Firstly, we need to run the `collector.py`, the collector will be waiting for data to be collected until we start the producer.

```bash
$ python3 collector.py
```

* Then, we will start the **consumers one by one**, run each command in a different terminal window.

```bash
$ python3 consumer.py
```

* Run the same command in another terminal.

```bash
$ python3 consumer.py
```

* Finally, we will start our producer that will start sending data to our pipeline.

```bash
$ python3 producer.py
```

31. Well done! :checkered_flag: You used ZeroMQ to develop messaging patterns!
