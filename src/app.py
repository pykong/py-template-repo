import typer
from loguru import logger

__all__ = ["app"]

app = typer.Typer()


@logger.catch
@app.command()
def hello(name: str) -> None:
    """Greet user by name.

    Args:
        name (str): The user's name.
    """
    logger.debug(f"hello called with name:{name}")
    typer.echo(f"Hello, {name}!")
