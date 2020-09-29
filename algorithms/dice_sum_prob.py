#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Probabilities for sums in rolling cubic dice

One popular way to study probability is to roll dice. A standard die has six
sides printed with little dots numbering 1, 2, 3, 4, 5, and 6. If the die is
fair (and we will assume that all of them are), then each of these outcomes
is equally likely. Since there are six possible outcomes, the probability of
obtaining any side of the die is 1/6. The probability of rolling a 1 is 1/6,
the probability of rolling a 2 is 1/6, and so on. But what happens if we add
another die? What are the probabilities for rolling two dice? three dice?
n number of dice?

I've solved that problem using recursion with the help of lru_cache decorator.
There are two functions you can use: 1 is for getting the list and 3 is for the
count. Use 3 if you're just interested in the probability. Don't change the
DEFAULT value, use MANUAL if you want to use 1 function.

Usage:
From terminal:
python dice_sum_prob.py <sum> <dice quantity>

------------------------- Examples ---------------------------
$ python dice_sum_prob.py 15 4

Possibilities: 140
Total: 1296
Probability: 0.10802469135802469
CacheInfo(hits=25, misses=18, maxsize=None, currsize=18)

$ python dice_sum_prob.py 25 10

Possibilities: 831204
Total: 60466176
Probability: 0.013746594459686023
CacheInfo(hits=440, misses=124, maxsize=None, currsize=124)

$ python dice_sum_prob.py 250 100

Possibilities: 313582961115880412311152190127564225946059591044116696715799107132080
Total: 653318623500070906096690267158057820537143710472954871543071966369497141477376
Probability: 4.799847269558915e-10
CacheInfo(hits=70659, misses=14550, maxsize=None, currsize=14550)

[MANUAL = 1]
$ python dice_sum_prob.py
Usage: python dice_sum_prob.py <sum> <dice quantity>
Enter the sum: 10
Enter the number of dice(s): 3
[   [1, 3, 6],
    [1, 4, 5],
    [1, 5, 4],
    [1, 6, 3],
    [2, 2, 6],
    [2, 3, 5],
    [2, 4, 4],
    [2, 5, 3],
    [2, 6, 2],
    [3, 1, 6],
    [3, 2, 5],
    [3, 3, 4],
    [3, 4, 3],
    [3, 5, 2],
    [3, 6, 1],
    [4, 1, 5],
    [4, 2, 4],
    [4, 3, 3],
    [4, 4, 2],
    [4, 5, 1],
    [5, 1, 4],
    [5, 2, 3],
    [5, 3, 2],
    [5, 4, 1],
    [6, 1, 3],
    [6, 2, 2],
    [6, 3, 1]]

NOTE: maxsize for the cache is None (infinite) for count function (3) but don't
keep it None for the list function (1) unless you have a large memory size :)
"""
from collections import OrderedDict
from functools import lru_cache
from pprint import pprint


# ---------------- all possible combinations in a list ----------------
@lru_cache(maxsize=128)  # Explicit is better than implicit
def possibilities_list(sum_, dice_amount) -> list:
    """
    Returns the list of all the possible combinations for a given sum and
    number of dice using lru_cache.

    Keeping the maxsize to a limit for the lru_cache is better usage.
    """
    poss = []
    if dice_amount == 2:
        for d1 in range(1, 7):
            for d2 in range(1, 7):
                if d1 + d2 == sum_:
                    poss.append([d1, d2])
    else:
        for dn in range(1, 7):
            if sum_ - dn < 2:
                continue
            for n in possibilities_list(sum_ - dn, dice_amount - 1):
                poss.append([dn] + n)
    return poss


# ------ Creating my own LRUCache class [For understanding purpose only] ------
# TODO: This is extremely basic, going to update it soon
class LRUCache:
    """Creates a LRUCache object for storing and retrieving values"""

    def __init__(self, capacity=128):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key) -> int:
        if key not in self.cache:
            return 0
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key, value) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if self.capacity:
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)


CACHED_COUNT = LRUCache()


def _possibilities_count(sum_, dice_amount) -> int:
    """
    Returns the total count of possibilities for a given sum and number of
    dice using LRUCache class.
    Using lru_cache is more efficient than this but this is more
    efficient than just using plain old dictionary.
    For understanding purpose only.
    """
    get_count = CACHED_COUNT.get((sum_, dice_amount))
    if get_count:
        return get_count
    poss_count = 0
    if dice_amount == 2:
        for d1 in range(1, 7):
            for d2 in range(1, 7):
                if d1 + d2 == sum_:
                    poss_count += 1
    else:
        for dn in range(1, 7):
            if sum_ - dn < 2:
                continue
            poss_count += _possibilities_count(sum_ - dn, dice_amount - 1)
    CACHED_COUNT.put((sum_, dice_amount), poss_count)
    return poss_count


# ----------------- all possible combinations as a count ----------------
@lru_cache(maxsize=None)  # Unlimited Cache. Use wisely
def possibilities_count(sum_, dice_amount) -> int:
    """
    Returns the total count of possibilities for a given sum and
    number of dice using lru_cache.

    Better than storing all the possible combinations in a list.
    It can even be used for more number of dices.
    """
    poss_count = 0
    if dice_amount == 2:
        for d1 in range(1, 7):
            for d2 in range(1, 7):
                if d1 + d2 == sum_:
                    poss_count += 1
    else:
        for dn in range(1, 7):
            if sum_ - dn < 2:
                continue
            poss_count += possibilities_count(sum_ - dn, dice_amount - 1)
    return poss_count


# ------------------ making use of all the above functions ------------------
if __name__ == "__main__":
    # TODO: Simplify!
    import sys

    FUNC_DICT = {
        1: possibilities_list,  # To get the list of all combinations
        2: _possibilities_count,  # For understanding purpose only
        3: possibilities_count,  # Just to get the count [DEFAULT]
    }

    DEFAULT = 3  # DON'T USE THIS
    MANUAL = 0  # Use this for different functions

    try:
        sum_, dice_quant = map(int, sys.argv[1:3])
        if sum_ > (dice_quant * 6):
            raise Exception(
                f"Sum cannot be more than {dice_quant * 6} for " f"{dice_quant} dices."
            )

        poss_count = FUNC_DICT[DEFAULT](sum_, dice_quant)
        total_poss = 6 ** dice_quant
        prob = poss_count / total_poss

        print(
            f"\nPossibilities: {poss_count}\n"
            f"Total: {total_poss}\n"
            f"Probability: {prob}\n"
            f"{FUNC_DICT[DEFAULT].cache_info()}"
        )  # Cache info

    except ValueError:
        print("Usage: python dice_sum_prob.py <sum> <dice quantity>")
    except Exception as err:
        print("Error:", err)

    if MANUAL:
        try:
            sum_ = int(input("Enter the sum: "))
            dice_quant = int(input("Enter the number of dice(s): "))

            if MANUAL == 1:
                poss_list = FUNC_DICT[MANUAL](sum_, dice_quant)
                pprint(poss_list, indent=4)
            elif MANUAL in [2, 3]:
                poss_count = FUNC_DICT[MANUAL](sum_, dice_quant)
                total_poss = 6 ** dice_quant
                prob = poss_count / total_poss

                print(
                    f"\nPossibilities: {poss_count}\n"
                    f"Total: {total_poss}\n"
                    f"Probability: {prob}"
                )

                if MANUAL == 3:
                    print(FUNC_DICT[MANUAL].cache_info())

        except ValueError:
            print("Not a number.")
