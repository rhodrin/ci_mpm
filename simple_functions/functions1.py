
from numpy import sqrt
from functools import cache

__all__ = ['my_sum', 'my_prod'] # module rsum 只是服务于计算pi，因此不需要导入


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot

def my_prod(iterable):
    result = 1
    for i in iterable:
        result *= i
    return result

@cache
def factorial(n):
    return n * factorial(n-1) if n else 1