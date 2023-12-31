from src.subpackage_one.module_1 import flip_coin


# INFO: This is just to demonstrate importing from src/ to tests/
def test_flip_coin():
    coin = flip_coin()
    assert coin in [True, False]
