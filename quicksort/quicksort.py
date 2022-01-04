def quicksort(array: list, lower: int, upper: int) -> None:
    """
    Recursive implementation of a Hoare partition scheme quicksort,
    with 'median of three' selection for the pivot.

    Arguments:
        array: the array to sort.
        lower: the lower bound of the partition of the array to sort.
        upper: the upper bound of the partition of the array to sort.
    """
    if lower >= 0 and upper >= 0 and lower < upper:
        partition_boundary = partition(array, lower, upper)
        quicksort(array, lower, partition_boundary)
        quicksort(array, partition_boundary + 1, upper)


def partition(array: list, lower: int, upper: int) -> int:
    """
    Apply Hoare partitioning to the input, return the partition boundary.

    Arguments:
        array: the array being sorted.
        lower: the lower bound of the partition of the array to further partition.
        upper: the upper bound of the partition of the array to further partition.
    """
    pivot = median_of_three(array, lower, upper)
    swap(array, pivot, upper - 1)
    i, j = lower, upper - 1
    
    while True:
        while array[i] < array[upper - 1]:
            i += 1
        while array[j] > array[upper - 1]:
            j -= 1
        if i >= j:
            swap(array, i, upper - 1)
            return j
        swap(array, i, j)


def median_of_three(array: list, lower: int, upper: int) -> int:
    """
    Choose the pivot of a partition by calculating the median of
    the first, middle and last element in the partition, sorting
    these three elements in place in the process.

    Arguments:
        partition: the array containing the partition.
        lower: the lower bound of the partition.
        upper: the upper bound of the partition.
    """
    mid = int((lower + upper) / 2)
    if array[lower] > array[mid]:
        swap(array, lower, mid)
    if array[mid] > array[upper]:
        swap(array, mid, upper)
    if array[lower] > array[mid]:
        swap(array, lower, mid)
    return mid


def swap(array: list, i: int, j: int) -> None:
    """
    Swaps the values at two indexes in a given list.

    Arguments:
        array: the list to swap values in.
        i: first index to swap from.
        j: second index to swap from.
    """
    array[i], array[j] = array[j], array[i]