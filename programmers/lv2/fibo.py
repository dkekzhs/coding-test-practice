from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    _curr, _next = 0, 1
    for _ in range(n):
        _curr, _next = _next, (_curr + _next)%1234567
    return _curr
def solution(n):
    return fib(n)

solution(5)