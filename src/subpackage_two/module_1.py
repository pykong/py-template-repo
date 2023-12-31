from ..subpackage_one import flip_coin


# INFO: This is just to demonstrate importing inter-package-wise
def pizza_or_hamburger() -> str:
    return "pizza" if flip_coin() else "hamburger"
