# Readme

## How to run

Execute:

`poetry run app 'Ben'`

You will see a logline and 'Hello, Ben!' printed on the console.

The above command calls a script entry point that internally invokes:

`poetry run python -m app 'Ben'`

### Running tests

`poetry run pytest`

See: https://python-poetry.org/docs/basic-usage/#using-poetry-run

## Links

- https://python-poetry.org/docs/
