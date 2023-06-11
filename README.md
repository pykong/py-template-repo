# Readme

## How to run

Execute:

`poetry run app 'Ben'`

You will see a logline and 'Hello, Ben!' printed on the console.

The above command calls a script entry point that internally invokes:

`poetry run python -m app 'Ben'`
