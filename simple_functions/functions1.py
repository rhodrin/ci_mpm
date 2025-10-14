
__all__ = ['my_sum']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i + 2
    return tot
