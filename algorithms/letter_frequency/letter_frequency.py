#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find the letter frequency from a given file.
https://wikipedia.org/wiki/Letter_frequencies.

Usage:
From terminal:
python3 letter_frequency.py <filename>
OR
python3 letter_frequency.py

NOTE:
File should be in the same directory as this script.
File should include the extension. (test.txt)

Example: [letter: (total count, frequency)]
$ python letter_frequency.py warandpeace.txt
{   'e': (313572, 12.436),
    't': (226412, 8.979),
    'a': (202719, 8.04),
    'o': (190084, 7.538),
    'n': (184185, 7.304),
    'i': (172257, 6.831),
    'h': (167415, 6.639),
    's': (162898, 6.46),
    'r': (148431, 5.887),
    'd': (118297, 4.691),
    'l': (96531, 3.828),
    'u': (64400, 2.554),
    'm': (61648, 2.445),
    'c': (61621, 2.444),
    'w': (59211, 2.348),
    'f': (54901, 2.177),
    'g': (51327, 2.036),
    'y': (46236, 1.834),
    'p': (45533, 1.806),
    'b': (34657, 1.374),
    'v': (27087, 1.074),
    'k': (20432, 0.81),
    'x': (4384, 0.174),
    'j': (2575, 0.102),
    'z': (2388, 0.095),
    'q': (2331, 0.092)}

Total letter count: 2521532
"""
import re
import pprint
from typing import Tuple, Dict
from operator import itemgetter


def letter_frequency(fhand) -> Tuple[Dict[str, Tuple[int, float]], int]:
    """
    Compute the frequency of each letter from a given file handle
    and store it in a dictionary

    fhand: file handle
    returns dictionary (str -> int)
    """
    letter_dict = {}
    letter_dict_get = letter_dict.get
    letters = re.compile(r'[a-z]')

    for line in fhand:
        letter_list = letters.findall(line.lower())
        for letter in letter_list:
            letter_dict[letter] = letter_dict_get(letter, 0) + 1

    total_val = sum(list(letter_dict.values()))

    letter_freq_sort = {
        let: (val, round(val / total_val * 100, 3))
        for let, val in sorted(
            letter_dict.items(), key=itemgetter(1), reverse=True
        )
    }

    return letter_freq_sort, total_val


def main(file: str = None):
    """
    Find letter frequency from a given file
    https://wikipedia.org/wiki/Letter_frequencies.
    """
    if not file:
        file_name = input("Enter file name: ")
    else:
        file_name = file

    try:
        with open(file_name, encoding='utf-8') as file_hand:
            letter_freq, total = letter_frequency(file_hand)
            pprint.pp(letter_freq, indent=4)
            print(f"\nTotal letter count: {total}\n")
    except OSError as err:
        print(err)


if __name__ == "__main__":
    import sys
    import os

    file = None

    try:
        file = sys.argv[1]
        filepath = os.path.join(os.getcwd(), file)
        if os.path.isfile(filepath):
            main(filepath)
        else:
            raise FileNotFoundError("File not found. Please make sure the file is "
                                    "in the same directory as this python script.")
    except FileNotFoundError as err:
        print("Error:", err)
    except IndexError:
        print("Usage: python3 letter_frequency.py <filename>")

    if not file:
        main()
