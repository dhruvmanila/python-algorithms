#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pascal's triangle:

Get the nth row of Pascal's triangle and the nth fibonacci number using
Pascal's triangle.

NOTE: As this algorithm uses recursion, the maximum number you can go to depends
on the recursion limit on your machine.

Terminal Usage:
Usage: python pascal_triangle.py <index>

Examples:
$ python pascal_triangle.py 4
[1, 3, 3, 1]

Fibonacci(4): 3

$ python pascal_triangle.py 14
[1, 13, 78, 286, 715, 1287, 1716, 1716, 1287, 715, 286, 78, 13, 1]

Fibonacci(14): 377

$ python pascal_triangle.py 65
[   1,
    64,
    2016,
    41664,
    635376,
    7624512,
    74974368,
    621216192,
    4426165368,
    27540584512,
    151473214816,
    743595781824,
    3284214703056,
    13136858812224,
    47855699958816,
    159518999862720,
    488526937079580,
    1379370175283520,
    3601688791018080,
    8719878125622720,
    19619725782651120,
    41107996877935680,
    80347448443237920,
    146721427591999680,
    250649105469666120,
    401038568751465792,
    601557853127198688,
    846636978475316672,
    1118770292985239888,
    1388818294740297792,
    1620288010530347424,
    1777090076065542336,
    1832624140942590534,
    1777090076065542336,
    1620288010530347424,
    1388818294740297792,
    1118770292985239888,
    846636978475316672,
    601557853127198688,
    401038568751465792,
    250649105469666120,
    146721427591999680,
    80347448443237920,
    41107996877935680,
    19619725782651120,
    8719878125622720,
    3601688791018080,
    1379370175283520,
    488526937079580,
    159518999862720,
    47855699958816,
    13136858812224,
    3284214703056,
    743595781824,
    151473214816,
    27540584512,
    4426165368,
    621216192,
    74974368,
    7624512,
    635376,
    41664,
    2016,
    64,
    1]

Fibonacci(65): 17167680177565

$ python pascal_triangle.py 1000
Error: maximum recursion depth exceeded in comparison
If you want to go much deeper, increase the recursion limit.

$ python pascal_triangle.py -142
Error: Index cannot be less than 1.

$ python pascal_triangle.py test
Error: invalid literal for int() with base 10: 'test'
"""
from pprint import pprint


def pascal_triangle(n):
    """Return the nth line in Pascal's triangle."""
    if n == 1:
        line = [1]
    else:
        line = [1]
        prev = pascal_triangle(n - 1)
        line.extend(prev[i] + prev[i + 1] for i in range(len(prev) - 1))
        line.append(1)
    return line


def fib_from_pascal(m):
    """Return the mth fibonacci number using Pascal's triangle."""

    def fib_pascal(n, fib_pos):
        if n == 1:
            line = [1]
            fib_sum = 1 if fib_pos == 0 else 0
        else:
            line = [1]
            prev, fib_sum = fib_pascal(n - 1, fib_pos + 1)
            line.extend(prev[i] + prev[i + 1] for i in range(len(prev) - 1))
            line.append(1)

            if fib_pos < len(line):
                fib_sum += line[fib_pos]
        return line, fib_sum

    return fib_pascal(m, 0)[1]


if __name__ == "__main__":
    # Usage: python pascal_triangle.py <index>
    import sys

    try:
        index = int(sys.argv[1])
        if index < 1:
            raise ValueError("Index cannot be less than 1.")
        num_list = pascal_triangle(index)
        fib_num = fib_from_pascal(index)
        pprint(num_list, indent=4)
        print(f"\nFibonacci({index}): {fib_num}")
    except IndexError:
        print("Usage: python pascal_triangle.py <index>")
    except ValueError as err:
        print("Error:", err)
    except RecursionError as err:
        print(
            f"Error: {err}\nIf you want to go much deeper, increase the recursion limit."
        )
