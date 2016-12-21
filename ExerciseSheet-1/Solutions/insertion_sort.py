#!/usr/bin/python3

""" Copyright 2016, University of Freiburg
    Bioinformatics Group
    Author: Michael Uhl
"""


def insertion_sort(lst):
    """ Sorting an integer list with the Insertion Sort algorithm.

    >>> insertion_sort([24, 6, 12, 32, 18])
    [6, 12, 18, 24, 32]

    >>> insertion_sort([0, 5, 0, -1])
    [-1, 0, 0, 5]

    >>> insertion_sort([])
    []
    """

    # Length of input list.
    n = len(lst)

    # Empty list.
    if (n == 0):
        return lst

    # Do the Insertion Sort.
    for i in range(1, n):
        element_to_insert = lst[i]
        # Look at already sorted list part.
        for j in range(i):
            if (element_to_insert < lst[j]):
                # Copy elements 1 to the right, decending.
                for k in range(i-1, j-1, -1):
                    lst[k+1] = lst[k]
                # Insert element at new position.
                lst[j] = element_to_insert
                break
    return lst


if __name__ == "__main__":
    # Create an unsorted list of integers.
    numbers = [5, 3, 1, 2, 8, 4]
    print("Input list:\n", numbers)
    # Sort the list.
    print("Sorted list:\n", insertion_sort(numbers))
