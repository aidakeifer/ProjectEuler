#!/usr/bin/env python3
import argparse


def next_factor(number):
    divisor = 1
    remainder = -1
    quotient = -1
    while remainder != 0:
        divisor += 1
        quotient = number // divisor
        remainder = number % divisor
    return quotient, divisor


def factor(number):
    factors = []
    while not (number == 1):
        number, divisor = next_factor(number)
        factors.append(divisor)
        if number == divisor:
            break
    return factors


def largest_factor(number):
    try:
        return factor(number)[-1]
    except IndexError:
        return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int)
    parser.add_argument('-a', '--all', action='store_true', default=False)
    args = parser.parse_args()
    factorfn = largest_factor
    if args.all:
        factorfn = factor
    print(factorfn(args.number))
