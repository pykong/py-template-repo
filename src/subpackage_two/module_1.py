from typing import Literal

from ..subpackage_one import flip_coin


# INFO: This is just to demonstrate importing inter-package-wise
def pizza_or_hamburger() -> Literal["pizza", "hamburger"]:
    """Chose between pizza and hamburger.

    Returns:
        str: The chosen food.
    """
    return "pizza" if flip_coin() else "hamburger"
