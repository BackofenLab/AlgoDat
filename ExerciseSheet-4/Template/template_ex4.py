#!/usr/bin/env python3

import codecs
import re

# import timeit


def read_word_list(path):
    """Read the encrypted text file and return the list of read words."""
    word_list = []
    regex = re.compile(r"[ ,.'\"*,^\r\n]|<.+?>", re.IGNORECASE)

    with open(path, encoding='utf-8') as file:
        for line in file.readlines():
            words = map(str.strip, regex.split(codecs.decode(line, 'rot13')))
            word_list.extend([word.lower() for word in words if len(word) >= 5])

    return word_list


def analyze_by_sorting(data):
    """Your method here.

    >>> Tests here"""
    return ranking


def analyze_by_map(data):
    """Your method here.

    >>> Tests here"""
    return ranking


def compute_runtimes(data):
    """Your method here."""
    # Output timing results


if __name__ == "__main__":
    word_data = read_word_list("test.encrypted.txt")
    # word_data = read_word_list("data.encrypted.txt")

    compute_runtimes(word_data)

    # Compute ranking here
    ...
