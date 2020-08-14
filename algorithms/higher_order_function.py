#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Higher order function operators:
This is just for understanding about higher order functions and
what is possible. It can also be used from the terminal.

Usage:
>>> eight(times(seven()))
56

>>> nine(divided_by(three()))
3.0

>>> two(minus(six()))
-4

>>> five(plus(one()))
6

>>> four(times(zero()))
0

>>> nine(modulus(eight()))
1

>>> one(divided_by(three()))
0.3333333333333333

>>> five(raise_to(five()))
25

Terminal Usage:
python higher_order_function.py <number> <operator> <number>
- number should be in words
- Supported operators: +, -, x, /, %, ^
"""

def zero(f=None):
    return 0 if f is None else f(0)

def one(f=None):
    return 1 if f is None else f(1)

def two(f=None):
    return 2 if f is None else f(2)

def three(f=None):
    return 3 if f is None else f(3)

def four(f=None):
    return 4 if f is None else f(4)

def five(f=None):
    return 5 if f is None else f(5)

def six(f=None):
    return 6 if f is None else f(6)

def seven(f=None):
    return 7 if f is None else f(7)

def eight(f=None):
    return 8 if f is None else f(8)

def nine(f=None):
    return 9 if f is None else f(9)


def plus(y):
    return lambda x: x + y

def minus(y):
    return lambda x: x - y

def times(y):
    return lambda x: x * y

def divided_by(y):
    return lambda x: x / y

def raise_to(y):
    return lambda x: x**y

def modulus(y):
    return lambda x: x % y


if __name__ == '__main__':
    import sys

    OPERATOR = {
        '+': 'plus',
        '-': 'minus',
        'x': 'times',
        '/': 'divided_by',
        '%': 'modulus',
        '^': 'raise_to'
    }

    try:
        args = sys.argv[1:4]
        num1, sign, num2 = map(lambda x: x.lower(), args)
        if any(val.isdecimal() for val in args):
            raise TypeError("Numbers should be in words. Eg., one, two, etc.")
        elif sign not in OPERATOR:
            raise TypeError(f"Supported operators: {', '.join(OPERATOR)}")

        oper = OPERATOR[sign]
        result = eval(num1 + '(' + oper + '(' + num2 + '()))')
        print(f"{num1} {sign} {num2} = {result}")

    except TypeError as err:
        print("Error:",err)
    except ValueError:
        print("Usage: "
            "python higher_order_function.py <number> <operator> <number>")
