#!/usr/bin/env python3
'''2520 is the smallest number that can be divided by
each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?'''

import argparse
from collections import Counter

'''
'''

def prime_factors(number):
    '''Find the prime factors of a number.
    This is a resonable method for smallish
    numbers and nothing more.'''
    factor = 2
    factors = []
    while factor ** 2 <= number:
        # we start by squaring the factor,
        # as it must be less than the sqrt of our number
        if number % factor:
            # if we have a remainder it is not a factor
            factor += 1
        else:
            # no remainder and we divide our number
            # and count the factor
            number //= factor
            factors.append(factor)
    if number > 1:
        # if we're left with more than 1 it must be prime
        factors.append(number)
    return factors


def smallest_multiple(start, end, step=1):
    '''Find the smallest number divisble by all the numbers in a given range.
    For example, the numbers 1 through 10 all divide 2520, and that is the smallest
    number for which that is true.

    The basic principle is this: find the prime factorization all the numbers in the
    range, and then figure out what the max number of each prime is within those
    numbers. Said another way, the prime factorization of the numbers 1 through 10 is:

        10 = 5*2
        9 = 3*3
        8 = 2*2*2
        7 = 7
        6 = 2*3
        5 = 5
        4 = 2*2
        3 = 3
        2 = 2
        1 = 1 (but this we can ignore)

    And if we factor 2520, we get:

        2520 = 2 * 2 * 2 * 3 * 3 * 5 * 7

    We see we get one 1, three 2s, two 3s, a 5, and a 7.

    From our factorization above, we notice that for all the numbers in the range,
    we only ever see one 7 (in 7), one 5 (in 10 and 5), but 9 has two 3s (one more than 6 and 3),
    and 8 has three 2s (one more than 4 and two more than 2). As such, the max occurance
    of these factors is the counts above that yield a product of 2520.
    '''
    max_factor_counts = {}
    for number in range(end, start, -step):
        factor_counts = Counter()

        # count the occurances of each factor
        for factor in prime_factors(number):
            try:
                factor_counts[factor] += 1
            except KeyError:
                factor_counts[factor] = 1

        # then see which are max counts for that factor and store
        for factor, count in factor_counts.items():
            max_factor_counts[factor] = max(max_factor_counts.get(factor, 0), count)

    # once we have all the max factor counts, simply
    # multiply everything together
    max_prod = 1
    for factor, count in max_factor_counts.items():
        max_prod *= factor ** count

    return max_prod


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description='Find the smallest number divisble by all the number in the given range'
    )
    parser.add_argument(
        'start',
        type=int,
        help='The lowest number in the range',
    )
    parser.add_argument(
        'end',
        type=int,
        help='The largest number in the range',
    )
    parser.add_argument(
        '-s',
        '--step',
        type=int,
        help='The step size used to move through the range; default 1',
        default=1,
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv=argv)
    print(smallest_multiple(args.start, args.end, step=args.step))


if __name__ == '__main__':
    main()

