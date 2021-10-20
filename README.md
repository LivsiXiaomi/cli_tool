# CLI Tool

## About The Project

This is a test project with cli tool which allow a user to create, move and delete directories.


## Getting Started

There are two way for running script: on local machine or using docker.

### Prerequisites

To run this project on your local machine without docker you need to install python ([download here](https://www.python.org/downloads/)).

### Installation
#### Local Machine
1) Create virtual env:
    - on Windows:
    ```
    python3 -m venv c:\path\to\myenv
    ```
    - on Linux:
    ```
    python3 -m venv /path/to/new/virtual/environment
    ```
2) Activate virtual env:
    - on Windows:
    ```
    c:\path\to\myenv\Scripts\activate.bat
    ```
    - on Linux:
    ```
    source /path/to/new/virtual/environment/bin/activate
    ```
3) Install requirements
    ```
    pip install -r requirements.txt
    ```
4) Set up PYTHONPATH env:
    - on Windows:
    ```
    set PYTHONPATH=%PYTHONPATH%;c:\path\to\project
    ```
    - on Linux:
    ```
    export PYTHONPATH="${PYTHONPATH}:/path/to/project"
    ```
#### Docker
1) Copy files with commands into `input_files` directories.
2) Build docker image:
```
docker build -f docker/Dockerfile -t cli_tool .
```

## Usage
#### Local Machine:
Before running the script you need to activate virtual env created on the previous step and create a file with commands.

To run the script execute next command:
- on Windows:
```
python3 src\cli.py --input_file=c:\path\to\test\file.txt
```
- on Linux:
```
python3 src/cli/py --input_file=/path/to/test/file.txt
```

after running the script, do not forget to turn off the virtual env:
```
deactivate
``` 

#### Docker:
To run the script execute next command:
```
docker run cli_tool --input_file=input_files/your/file/name.txt
```