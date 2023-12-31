# Readme

## How to run

Execute:

`poetry run src 'Ben'`

You will see a logline and 'Hello, Ben!' printed on the console.

The above command calls a script entry point that internally invokes:

`poetry run python -m src 'Ben'`

To see all possible command targets invoke the `typer` help.

`poetry run src --help`

### Running tests

`poetry run pytest`

See: <https://python-poetry.org/docs/basic-usage/#using-poetry-run>

## Links

- [Poetry Docs](https://python-poetry.org/docs/)
- [Python Docs: Modules & Packages](https://docs.python.org/3/tutorial/modules.html#packages)
