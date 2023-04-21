import typer

app = typer.Typer()


@app.command()
def hello(name: str) -> None:
    """Greet user by name.

    Args:
        name (str): The user's name.
    """
    typer.echo(f"Hello, {name}!")


if __name__ == "__main__":
    app()
