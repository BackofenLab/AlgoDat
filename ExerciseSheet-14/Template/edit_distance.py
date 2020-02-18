#!/usr/bin/python3

import sys


def compute_ed_recursively(x, y):
    """ Compute edit distance from x to y recursively.

    >>> compute_ed_recursively("", "")
    0
    >>> compute_ed_recursively("donald", "ronaldo")
    2
    """
    n = len(x)
    m = len(y)
    if n == 0:
        return m
    if m == 0:
        return n
    # Insert case.
    ed1 = compute_ed_recursively(x, y[0:-1]) + 1
    # Delete case.
    ed2 = compute_ed_recursively(x[0:-1], y) + 1
    # Replace case.
    ed3 = compute_ed_recursively(x[0:-1], y[0:-1])
    # If last characters do not match, add replace costs.
    if x[-1] != y[-1]:
        ed3 += 1
    return min(ed1, ed2, ed3)


def compute_ed_via_table(x, y):
    """ Compute edit distance via dynamic programming table.

    >>> compute_ed_recursively("", "")
    0
    """
    return 0


if __name__ == "__main__":
    # Read in two strings from command line.
    nr_args = len(sys.argv)
    if not nr_args == 3:
        raise Exception("script excepts two input strings")
    x = sys.argv[1]
    y = sys.argv[2]
    print("x = %s" % (x))
    print("y = %s" % (y))
    ed = compute_ed_recursively(x, y)
    print("Edit distance (x -> y): %i" % (ed))
