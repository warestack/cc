### Lab1.3: Developing a Cloud service using Python (homework :construction_worker:)

#### What am I about to learn?

Today's lab session is essential to have a solid start in this module. Make sure you complete all the tasks before the next class.

Lab 1 part 3 focuses on how to:

**Lab 1.3**    Develop a simple cloud service :cloud: using Python.

#### Lab 1.3: **Developing a simple cloud service with Python** 

Your task is to develop a data generator in Python (called `generator.py`) and **run it in your VM**. A second service, (called `collector.py`) will connect to your generator (or your colleague’s `generators`) to collect and display the data.

:muscle: To develop this simple service, you will need the following:

* Check online about the `requests` library.
* You will need to improvise and follow the tasks.

##### Task 1

*  Create a Python file called `generator.py`. The program should generate a  JSON dataset similar to the following.

```json
{"server0": 19, "server1": 47, "server2": 89, "server3": 3, "server4": 9, "server5": 21, "server6": 68, "server7": 66, "server8": 97, "server9": 42}
```

> “server0”, “server1” etc. are presumably the names of cloud servers, and 19, 47, etc. are their corresponding CPU resource usage. 
>
> The numbers are randomly generated using the Python `random` library.
>
> The resource usage value is a random integer between 0 and 100.

* Save your data as `data.json`

> Make sure you store your data.json file in the `/var/www/html` folder to be accessible through the Apache2 web server, e.g. by visiting your `URL/data.json` as shown below.

<img src="https://github.com/steliosot/cc-images/blob/main/Output-server.png?raw=true" alt="Watch the video" style="zoom:60%;" />

> :rotating_light: You need to save your data in the Apache2 directory as a `sudoer`, and you will need to run the Python script as sudo.
>
> :mag: You might need to check online how to **dump** data to a JSON file, and check out the Python **enumerate** method. There are multiple ways to generate this data, so feel free to improvise.

##### Task 2

Create a Python file, called `collector.py` to read the `data.json` by using the VM’s URL (`URL/data.json`) .

* Run this script in your local computer (or in google Colab)
* Count how many servers are under and over-utilized.
  * Values between 0-49 are classified as under-utilized; 
  * Values between 50-100 are classified as over-utilized.
  * Print the results, for example, my results look like this:

```python
server0 41
server1 55
server2 10
server3 75
server4 93
server5 78
server6 24
server7 70
server8 95
server9 7
{'under': 4, 'over': 6}
```

##### Stretch activity

Adapt your script to connect to other data generators, e.g. one of your friends.

>  You can change the IP of your code using the following trick.
>
> :rotating_light: Pass the IP as an argument to your python command, see an example:

```shell
$ python3 collector.py http://111.111.1.1/data.json
```

> * The URL IP address `http://111.111.1.1/` is the **external IP** of my GCP VM.
>
> * The complete URL: `http://111.111.1.1/data.json` maps to the address of the generator that in turn `renders` (shows) the data available in `/var/www/html/data.json`

To get arguments from the command line try the following code in your Python script:

```python
import sys
print(sys.argv[0])
print(sys.argv[1])
```

:mag: Check online: Command Line Arguments in Python