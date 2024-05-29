# FastUI as Sub-Application

Example, in response to these two issues: [pydantic/FastUI#311](https://github.com/pydantic/FastUI/issues/311) and [pydantic/FastUI#134](https://github.com/pydantic/FastUI/issues/134), of using FastUI as a sub-application.

## How to run

### Clone the repo

```shell
git clone https://github.com/hasansezertasan/fastui-tutorials.git
cd fastui-tutorials
```

### Change directory to the example

```shell
cd examples/sub-application
```

### Create a virtual environment

- Create and activate a virtual environment:

```shell
python3 -m venv venv
source venv/bin/activate
```

### Install the requirements

```shell
pip install -r 'requirements.txt'
```

### Run the application

```shell
uvicorn main:app
```
