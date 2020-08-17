#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Greatest Common Divisor
Usage:
From terminal:
python3 gcd.py <num1> <num2>
OR
python3 -m gcd <num1> <num2>

Extras:
There are three functions shown below. You can add your own function and
add it to the FUNC_DICT with the appropriate key value (preferably ordered numbers)
and change the value of DEFAULT to use that function.

Examples: (Change DEFAULT to determine which function to use)
$ python gcd.py 14 20
GCD using 'gcd_euclidean': 2

$ python gcd.py 14876 9864
GCD using 'gcd_euclidean_mod': 4

$ python gcd.py 343 2408
GCD using 'gcd_stein': 7
"""


# Euclidean algorithm (Using subtraction)
def gcd_euclidean(num1: int, num2: int) -> int:
    a, b = num1, num2
    while a != b:
        a, b = max(a, b), min(a, b)
        a -= b
    return a


# Efficient Euclidean algorithm (Using mod)
def gcd_euclidean_mod(num1: int, num2: int) -> int:
    gcd, sentinel = num1, num2
    while sentinel:
        gcd, sentinel = sentinel, gcd % sentinel
    if (num2 or num1) < 0:
        return -gcd
    return gcd


# Stein's algorithm or Binary algorithm
# Using bitwise operators to determine the parity of a and b:
# Examples:
# For 9:
#        9 ->        1 0 0 1
#        1 ->     &  0 0 0 1
#        -------------------
#        result->    0 0 0 1
# So 9 AND 1 gives us 1, as the right most bit of every odd number is 1
#
# For 14:
#        14 ->      1 1 1 0
#        1  ->   &  0 0 0 1
#        ------------------
#        result->   0 0 0 0
# So 14 AND 1 gives us 0, as the right most bit of every even number is 0.
def gcd_stein(num1: int, num2: int) -> int:
    a, b = num1, num2
    d = 0
    while a != b:
        if not(a & 1) and not(b & 1):
            a //= 2
            b //= 2
            d += 1
        elif not(a & 1) and (b & 1):
            a //= 2
        elif (a & 1) and not(b & 1):
            b //= 2
        else:
            a, b = max(a, b), min(a, b)
            a -= b
    gcd = a * pow(2, d)
    return gcd


if __name__ == '__main__':
    # Usage: python gcd.py <num1> <num2>
    import sys

    # Add your own function here (Only the function name and no quotes).
    FUNC_DICT = {
        1: gcd_euclidean,
        2: gcd_euclidean_mod,
        3: gcd_stein
    }

    DEFAULT = 3  # From FUNC_DICT

    try:
        num1, num2 = map(int, sys.argv[1:3])
        gcd = FUNC_DICT[DEFAULT](num1, num2)
        print(f"GCD using '{FUNC_DICT[DEFAULT].__name__}': {gcd}\n")
    except ValueError:
        print("Usage: python gcd.py <num1> <num2>")
