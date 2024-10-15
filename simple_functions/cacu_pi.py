
from numpy import sqrt
from functions1 import factorial
from functools import cache

__all__ = ['pi']


def pi(terms=1):
    return 1./(2.*sqrt(2.)/9801.*rsum(terms))


@cache  # 递归/重复调用时记得使用 @cache
def rsum(n):
    t = factorial(4*n)*(1103+26390*n)/(factorial(n)**4*396**(4*n))
    return t + rsum(n-1) if n else t

print(pi(100))