import pytest


def check(x, y):
    assert x ** x == y


def test_squared():
    yield check, 2, 4
    yield check, 3, 9


@pytest.mark.parametrize("x, y", [(2, 4), (3, 9)])
def test_squared(x, y):
    assert x ** x == y