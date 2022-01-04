def insertion_sort(array: list) -> None:
    """
    Implementation of insertion sort.

    Arguments:
        array: the array to sort.
    """
    for i, _ in enumerate(array):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j, j - 1)
            j -= 1
    

def swap(array: list, i: int, j: int) -> None:
    """
    Swaps the values at two indexes in a given list.

    Arguments:
        array: the list to swap values in.
        i: first index to swap from.
        j: second index to swap from.
    """
    array[i], array[j] = array[j], array[i]