import typer
from loguru import logger

# INFO: This is just to demonstrate importing from a subpackage
from .subpackage_one import flip_coin, flip_n_coins
from .subpackage_two import pizza_or_hamburger

__all__ = ["cli"]

cli = typer.Typer()


@logger.catch
@cli.command()
def hello(name: str) -> None:
    """Greet user by name.

    Args:
        name (str): The user's name.
    """
    logger.debug(f"hello called with name:{name}")
    typer.echo(f"Hello, {name}!")


@logger.catch
@cli.command()
def flip_coins(flip_n_times: int) -> None:
    """Flip a coin.

    Args:
        flip_n_times (int): The number of coin flips.

    Raises:
        ValueError: If flip_n_times is < 1.
    """
    if not flip_n_times:
        raise ValueError("flip_n_times must be > 0")
    elif flip_n_times == 1:
        coin = flip_coin()
        logger.debug(f"subpackage_one.flip_coin: {coin}")
        typer.echo(f"Coin: {coin}!")
    else:
        coins = flip_n_coins(flip_n_times)
        logger.debug(f"subpackage_one.flip_n_coins: {coins}")
        typer.echo(f"Coin: {coins}!")


@logger.catch
@cli.command()
def chose_food() -> None:
    """Chose what to eat tonight."""
    food = pizza_or_hamburger()
    logger.debug(f"subpackage_two.chose_food: {food}")
    typer.echo(f"Tonight we'll eat: {food}!")
