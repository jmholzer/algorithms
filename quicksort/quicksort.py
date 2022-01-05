def quicksort(array: list, lower: int, upper: int):
    """
    Implementation of quicksort using Lomuto partitioning, with
    simple pivot selection.

    Arguments:
        array: the array to sort.
        lower: the lower bound of the partition of the array to sort.
        upper: the upper bound of the partition of the array to sort.
    """
    if lower < upper:
        partition_boundary = partition(array, lower, upper)
        quicksort(array, lower, partition_boundary - 1)
        quicksort(array, partition_boundary + 1, upper)


def partition(array: list, lower: int, upper: int) -> int:
    """
    Apply Lomuto partitioning to the partition defined in the input.

    Arguments:
        array: the array being sorted.
        lower: the lower bound of the partition to (further) partition.
        upper: the upper bound of the partition to (further) partition.
    """
    pivot = array[lower]

    i = lower
    for j in range(lower, upper + 1):
        if array[j] < pivot:
            i += 1
            swap(array, i, j)
    swap(array, lower, i)
    return i


def swap(array: list, i: int, j: int) -> None:
    """
    Swaps the values at two indexes in a given list.

    Arguments:
        array: the list to swap values in.
        i: first index to swap from.
        j: second index to swap from.
    """
    array[i], array[j] = array[j], array[i]