from .module_1 import flip_coin


# INFO: This is just to demonstrate importing intra-package-wise
def flip_n_coins(n: int) -> list[bool]:
    """Flip n coins.

    Args:
        n (int): The number of coin flips.

    Returns:
        list[bool]: The results of the coin flips.
    """
    return [flip_coin() for _ in range(n)]
