def merge_sort(array: list, lower: int, upper: int) -> None:
    """
    Top-down implementation of merge sort.

    Arguments:
        array: the array being sorted.
        lower: the lower bound of the partition ('half') of the array to sort.
        upper: the upper bound of the partition ('half') of the array to sort.
    """
    if lower >= upper:
        return

    mid = int((lower + upper) / 2)
    merge_sort(array, lower, mid)
    merge_sort(array, mid + 1, upper)
    merge_halves(array, lower, upper)


def merge_halves(array: list, lower: int, upper: int) -> None:
    """
    Merges two halves of the given partition of the array being sorted,
    sorting them as it does so and saving the result in place.

    Arguments:
        array: the array being sorted.
        lower: the lower bound of the partition of the array.
        upper: the upper bound of the partition of the array.
    """
    mid = int((lower + upper) / 2)
    
    left = array[lower:mid + 1]
    right = array[mid + 1:upper + 1]

    index = 0
    while left and right:
        if left[0] < right[0]:
            array[lower + index] = left[0]
            left = left[1:]
        else:
            array[lower + index] = right[0]
            right = right[1:]
        index += 1

    # Either left or right may have elements left, consume these.
    while left:
        array[lower + index] = left[0]
        left = left[1:]
        index += 1
    while right:
        array[lower+ index] = right[0]
        right = right[1:]
        index += 1