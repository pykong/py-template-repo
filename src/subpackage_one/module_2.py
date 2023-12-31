from .module_1 import flip_coin


# INFO: This is just to demonstrate importing intra-package-wise
def flip_n_coins(n: int) -> list[bool]:
    return [flip_coin() for _ in range(n)]
