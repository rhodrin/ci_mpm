from numpy import sqrt
from simple_functions.functions1 import factorial
from functools import cache  # lru_cache is a older version

__all__ = ["pi", "rsum"]


def pi(terms=1):
    return 1.0 / (2.0 * sqrt(2.0) / 9801.0 * rsum(terms))


@cache
def rsum(n):
    t = (
        factorial(4 * n)
        * (1103 + 26390 * n)
        / (factorial(n) ** 4 * 396 ** (4 * n))
    )
    return t + rsum(n - 1) if n else t
