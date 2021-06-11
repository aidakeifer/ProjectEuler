#!/usr/bin/env python
def a(m, n):
    return m**2 - n**2

def b(m, n):
    return 2 * m * n

def c(m, n):
    return n**2 + m**2

SUM=1000
m = 1
_sum = 0
_c = 0
while _sum != SUM and _c <= SUM:
    m += 1
    n = 1
    while n < m and _sum != SUM and _c <= SUM:
        _a = a(m, n)
        _b = b(m, n)
        _c = c(m, n)
        _sum = _a + _b + _c
        n += 1

print(_a, _b, _c, _sum, _a*_b*_c)
