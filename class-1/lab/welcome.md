### Welcome to Week 1

This week, you will build your first API using Python and FastAPI. An **API (Application Programming Interface)** lets programs request information from one another. You will start with a welcome message, then build routes that return movie and student data.

Before starting Part 1, take a few minutes to prepare your tools.

#### Install and Check Python

**Python** is the programming language you will use to build your API. You need Python installed on your computer to run the code in these labs.

First, check whether Python is already installed. Open **Terminal** on macOS/Linux or **PowerShell** on Windows. A terminal lets you type commands to run programs.

On macOS/Linux, run:

```bash
python3 --version
```

On Windows PowerShell, run:

```powershell
python --version
```

If `python` is not recognised on Windows, try `py --version`.

You should see a Python version number. Use **Python 3.10 or later**, which is required by the FastAPI and Uvicorn versions used in these labs.

If Python is missing or your version is older than 3.10, download a suitable installer for your operating system from the [official Python website](https://www.python.org/downloads/) and follow its installation instructions. Then close and reopen your terminal and check again. Ask your tutor if you need help setting it up.

#### Install Visual Studio Code

**Visual Studio Code (VS Code)** is a free code editor. You will use it to create project folders, write Python code, and run commands in its built-in terminal.

1. Visit the [official VS Code website](https://code.visualstudio.com/).
2. Download the desktop version for your operating system: Windows, macOS, or Linux.
3. Open the downloaded file and follow the installation instructions for your system.
4. Open **Visual Studio Code** once installation is complete.

If you already have VS Code installed, you can use your existing installation.

VS Code is the editor; Python runs your code. Installing VS Code does not install Python.

Select **Terminal > New Terminal** in VS Code and repeat the Python version check above. You will use this built-in terminal to run commands during Part 1.

#### What Is a Virtual Environment?

A **virtual environment**, often called a **venv**, gives a Python project its own set of installed packages. Packages are extra tools your code can use, such as FastAPI.

Different projects may need different versions of the same package. A virtual environment keeps those versions separate, so installing packages for one project does not change another project's environment.

In these labs, each new project will have a virtual environment stored in a folder called `.venv`. You create it once for that project and activate it whenever you open a new terminal to work on the project. Activation tells the terminal to use that environment's Python and packages.

Part 1 will guide you through creating and activating your first virtual environment.

#### Ready to Begin?

Once VS Code is installed and your Python version check works, proceed to [Part 1: Create Your First FastAPI App](part-1.md).
