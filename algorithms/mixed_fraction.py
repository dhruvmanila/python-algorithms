#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert fraction into mixed fraction from the terminal.

Terminal Usage:
python mixed_fraction.py <numerator/denominator>
- Make sure to put the forward slash to separate the numerator and denominator.

Examples:
$ python mixed_fraction.py 123/435
Mixed fraction: 41/145

$ python mixed_fraction.py 2535/234
Mixed fraction: 10 5/6

$ python mixed_fraction.py 25283975364/14338756
Mixed fraction: 1763 1187134/3584689

$ python mixed_fraction.py 96783975323423564/68245338756
Mixed fraction: 1418177 1385613938/17061334689

$ python mixed_fraction.py
Usage: python mixed_fraction.py <numerator/denominator>
Enter a fraction of type 'num/denom': 9834/234
Mixed fraction: 42 1/39
"""
from typing import Tuple


def _irreducible_fraction(num: int, denom: int) -> Tuple[int, int]:
    gcd, sentinel = num, denom
    while sentinel:
        gcd, sentinel = sentinel, gcd % sentinel
    if (denom or num) < 0:
        gcd = -gcd
    num //= gcd
    denom //= gcd
    return num, denom


def mixed_fraction(fraction: str) -> str:
    if not isinstance(fraction, str):
        raise TypeError("Argument should be of string type of the form: 'x/y'")

    if "/" in fraction:
        try:
            numerator, denominator = (int(i) for i in fraction.split("/"))
        except ValueError:
            raise ValueError(
                "Invalid argument value. Maybe you forgot to " "add forward slash?"
            ) from None

        if not denominator:
            raise ZeroDivisionError("Denominator cannot be 0.")

        sign = (
            "-"
            if (numerator > 0 > denominator) or (numerator < 0 < denominator)
            else ""
        )
        num, denom = _irreducible_fraction(abs(numerator), abs(denominator))
        integer, remainder = divmod(num, denom)

        if not remainder:
            return "{}{}".format(sign, integer)
        elif not integer:
            return "{}{}/{}".format(sign, num, denom)
        else:
            return "{}{} {}/{}".format(sign, integer, remainder, denom)
    else:
        return fraction


if __name__ == "__main__":
    # Usage: python mixed_fraction.py <numerator/denominator>
    import sys

    result = None

    try:
        frac = sys.argv[1]
        result = mixed_fraction(frac)
        print(f"Mixed fraction: {result}")
    except IndexError:
        print("Usage: python3 mixed_fraction.py <numerator/denominator>")

    if not result:
        frac = input("Enter a fraction of type 'num/denom': ")
        result = mixed_fraction(frac)
        print(f"Mixed fraction: {result}")
