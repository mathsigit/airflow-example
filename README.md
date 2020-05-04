# airflow-example

In this example, all the command would operator via `MacOS` OS.

## Requirement

* Python 3.6/3.7
* [Virtualenv](https://virtualenv.pypa.io/en/stable/)
* [Homebrew](https://brew.sh/)
* Hadoop 2.8.x.
* JDK 8

## Python3 Virtualenv Setup

```bash
$ brew install python3
```

Pip3 is installed with Python3

### Installation
To install virtualenv via pip run:
```bash
$ pip3 install virtualenv
```

### Usage
Creation of virtualenv:
```bash
$ virtualenv -p python3 airflow-example/venv
```

Activate the virtualenv:
```bash
$ source venv/bin/activate
```

Deactivate the virtualenv:
```bash
$ deactivate
```

## Setting worker node 
1. Downloading th hadoop 2.8.x and setting up configuration for connecting to the target hadoop cluster.
2. Downloading and unzipping the JDK8.
3. Editing the t2 `bash_command` of `src/airflow/dag_from_file.py` to conform with your usage scenarios.

## Directory of this example

```shell script
├── README.md            ## Readme file
├── src                  ## DAG of Airflow(python source code)
│   └── airflow
└── venv                 ## Path of Virtualenv(pip3), and all the airflow library would be installed here.
    ├── bin
    │   └── __pycache__
    ├── include
    └── lib
        └── python3.7
```