def counting_sort(array: list) -> list:
    """
    An implementation of counting sort for use with arrays of integers.

    Arguments:
        array: the array to sort.
    """
    count = [0 for _ in range(max(array) + 1)]
    output = [0 for _ in array]
    
    for i in array:
        count[i] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    count = [0] + count[:-1]

    for i in array:
        output[count[i]] = i
        count[i] += 1

    return output