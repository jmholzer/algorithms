def bubble_sort(array: list) -> None:
    """
    Implementation of bubble sort.

    Arguments:
        array: the array to sort.
    """
    for _ in range(1, len(array)):
        for j in range(0, len(array) - 1):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)


def swap(array: list, i: int, j: int) -> None:
    """
    Swaps the values at two indexes in a given list.

    Arguments:
        array: the list to swap values in.
        i: first index to swap from.
        j: second index to swap from.
    """
    array[i], array[j] = array[j], array[i]