#!/usr/bin/env python3
import argparse


def is_prime(number):
    divisor = 1
    remainder = -1
    quotient = -1
    while remainder != 0:
        divisor += 1
        quotient = number // divisor
        remainder = number % divisor

    if quotient == 1:
        return True
    return False


def faster_is_prime(number):
    divisor = 2
    while divisor**2 <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def nth_prime(n, return_all=False):
    all = [2] if return_all else None

    if n == 1:
        return all if all else 2

    _next = 1
    while n > 1:
        _next += 2
        if faster_is_prime(_next):
            if all is not None:
                all.append(_next)
            n -= 1
    return all if all else _next


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int)
    parser.add_argument('--all', action='store_true', default=False)
    parser.add_argument('--diffs', action='store_true', default=False)
    args = parser.parse_args()

    nth = nth_prime(args.number, return_all=(args.all or args.diffs))

    if args.diffs:
        diffs = []
        for i in range(len(nth)-1):
            diffs.append(nth[i+1] - nth[i])
        print(diffs)
    else:
        print(nth)
