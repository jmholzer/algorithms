from typing import Any

def binary_search(array: list, key: Any):
    """
    Performs a binary search on a sorted array.

    Arguments:
        array: the array to search through.
        key: the value to search for.
    """

    lower_bound, upper_bound = 0, len(array) - 1
    while lower_bound <= upper_bound:
        midpoint = int((lower_bound + upper_bound) / 2)
        if array[midpoint] < key:
            lower_bound = midpoint + 1
        elif array[midpoint] > key:
            upper_bound = midpoint - 1
        else:
            return midpoint
    return None