from random import random


def flip_coin() -> bool:
    """Flip a coin.

    Returns:
        bool: Heads or tails.
    """
    return random() < 0.5  # noqa: PLR2004
