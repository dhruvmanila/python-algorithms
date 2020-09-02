#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Encode or decode morse code right from the terminal.

Usage:
python3 morse_code.py <encode/decode> <'message'>

NOTE:
- Message should be enclosed within quotes (single/double), but make sure to use
  the opposite in your message. If you're enclosing your message in double quotes then use
  single inside and vice versa.

Tests:
$ python morse_code.py
Usage: python morse_code.py <encode/decode> <'message'>

$ python morse_code.py test
Error: Mode can only be either 'encode' or 'decode'.

$ python morse_code.py encode
Error: Message cannot be empty.

$ python morse_code.py encode this is a test
Error: Message entered has to be enclosed within quotes.

$ python morse_code.py decode 'this is a test'
Error: 'this' not in morse code dictionary. Did you mean to encode?

$ python morse_code.py encode 'this is a test'
- .... .. ...    .. ...    .-    - . ... -

$ python morse_code.py encode '       this is a test    '
- .... .. ...    .. ...    .-    - . ... -

$ python morse_code.py decode '- .... .. ...    .. ...    .-    - . ... -'
this is a test

$ python morse_code.py decode '   - .... .. ...    .. ...    .-    - . ... -       '
this is a test
"""

encode_morse = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "...--",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ",": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    ";": "-.-.-",
    ":": "---...",
    "/": "-..-.",
    "-": "-....-",
    "'": ".----.",
    "(": "-.--.-",
    ")": "-.--.-",
    "[": "-.--.-",
    "]": "-.--.-",
    "{": "-.--.-",
    "}": "-.--.-",
    "_": "..--.-",
    "+": ".-.-.",
    "=": "-...-",
    "&": ".-...",
    "@": ".--.-.",
    "!": "-.-.--",
}

decode_morse = dict(zip(encode_morse.values(), encode_morse.keys()))


def encode_txt(text, key):
    code = ""
    for let in text.strip().lower():
        if let == " ":
            code += "   "
        else:
            code += key[let] + " "
    return code[:-1]


def decode_txt(text, key):
    decode = ""
    words = text.strip().split("   ")
    for word in words:
        for char in word.split():
            decode += key[char]
        decode += " "
    return decode[:-1]


if __name__ == "__main__":
    import sys

    MODE = ["encode", "decode"]

    try:
        mode = sys.argv[1]
        msg = sys.argv[2:]
        if mode not in MODE:
            raise ValueError("Mode can only be either 'encode' or 'decode'.")
        elif not msg:
            raise ValueError("Message cannot be empty.")
        elif len(msg) > 1:
            raise ValueError("Message entered has to be enclosed within quotes.")

        if mode == "encode":
            encrypt = encode_txt(msg[0], encode_morse)
            print(encrypt)
        elif mode == "decode":
            decrypt = decode_txt(msg[0], decode_morse)
            print(decrypt)

    except ValueError as err:
        print(f"Error: {err}")
    except KeyError as err:
        print(f"Error: {err} not in morse code dictionary. Did you mean to encode?")
    except Exception:
        print("Usage: python morse_code.py <encode/decode> <'message'>")
