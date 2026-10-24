# BlackSheep and FastUI

> See [Other web frameworks](../../docs/tutorial/08-other-frameworks.md) in the tutorial for how the framework examples compare.

This is a simple example project that shows how to use FastUI with BlackSheep.

It exposes two routes:

- `/api/` returns the FastUI component tree as JSON.
- Every other path serves the FastUI React shell.

## How to run

### Clone the repo

```shell
git clone https://github.com/hasansezertasan/fastui-tutorials.git
cd fastui-tutorials
```

### Change directory to the example

```shell
cd examples/with-blacksheep
```

### Run the application

```shell
uv run with-blacksheep
```

Then open `http://127.0.0.1:8000`.
