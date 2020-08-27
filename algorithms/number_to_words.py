#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert numbers into words from the terminal.

Terminal Usage:
python3 number_to_words.py <number>

Examples:
$ python number_to_words.py 16
16: sixteen

$ python number_to_words.py 546
546: five hundred forty-six

$ python number_to_words.py 523786
523786: five hundred twenty-three thousand seven hundred eighty-six

$ python number_to_words.py 8761278529
8761278529: eight billion seven hundred sixty-one million two hundred seventy-eight thousand five hundred twenty-nine

$ python number_to_words.py
Usage: python3 number_to_words <number>
Enter a number: test
Error: Invalid input.

$ python number_to_words.py
Usage: python3 number_to_words <number>
Enter a number: 6363234
6363234: six million three hundred sixty-three thousand two hundred thirty-four

$ python number_to_words.py 999999999999999
999999999999999: nine hundred ninety-nine trillion nine hundred ninety-nine billion nine hundred ninety-nine million nine hundred ninety-nine thousand nine hundred ninety-nine

$ python number_to_words.py 1000000000000000
1000000000000000: Support upto 999,999,999,999,999 (1 less than a quadrillion)
"""

WORDS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"
]


def number_to_words(n):
    """
    Convert numbers into words.
    Supports from 0 upto 999,999,999,999,999 (1 less than a quadrillion).
    Uses recursion.
    """
    if n < 20:
        return WORDS[n]
    elif n < 100:
        return WORDS[18 + n // 10] + ('' if n % 10 == 0 else '-' +
                                                             WORDS[n % 10])
    elif n < 1_000:
        return number_to_words(n // 100) + " hundred" + \
               (' ' + number_to_words(n % 100) if n % 100 > 0 else '')
    elif n < 1_000_000:
        return number_to_words(n // 1_000) + " thousand" + \
               (' ' + number_to_words(n % 1_000) if n % 1_000 > 0 else '')
    elif n < 1_000_000_000:
        return number_to_words(n // 1_000_000) + " million" + \
               (' ' + number_to_words(n % 1_000_000) if n % 1_000_000 > 0
                else '')
    elif n < 1_000_000_000_000:
        return number_to_words(n // 1_000_000_000) + " billion" + \
               (' ' + number_to_words(n % 1_000_000_000)
                if n % 1_000_000_000 > 0 else '')
    elif n < 1_000_000_000_000_000:
        return number_to_words(n // 1_000_000_000_000) + " trillion" + \
               (' ' + number_to_words(n % 1_000_000_000_000)
                if n % 1_000_000_000_000 > 0 else '')
    else:
        return "Support upto 999,999,999,999,999 (1 less than a quadrillion)"


if __name__ == '__main__':
    import sys
    word = None

    try:
        num = int(sys.argv[1])
        word = number_to_words(num)
        print(f"{num}: {word}")
    except (IndexError, ValueError):
        print("Usage: python3 number_to_words <number>")

    if not word:
        try:
            num = int(input("Enter a number: "))
            word = number_to_words(num)
            print(f"{num}: {word}")
        except ValueError:
            print("Error: Invalid input.")
