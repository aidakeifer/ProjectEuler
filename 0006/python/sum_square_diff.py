#!/usr/bin/env python3
"""
The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

import argparse


def sum_squares(n):
    sum = 0
    for num in range(n):
        sum += (num+1)**2
    return sum


def square_sums(n):
    sum = 0
    for num in range(n):
        sum += num + 1
    return sum**2


def positive_int(arg):
    try:
        arg = int(arg)
    except TypeError:
        raise argparse.ArgumentError('Not a postive integer')

    if arg <= 0:
        raise argparse.ArgumentError('Not a postive integer')

    return arg


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('count', type=positive_int)
    args = parser.parse_args()
    print(square_sums(args.count) - sum_squares(args.count))
