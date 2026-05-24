def linear_search(values, target):
    """Return the index of target in values, or -1 when missing."""
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def binary_search(values, target):
    """Return the index of target in a sorted sequence, or -1 when missing."""
    left = 0
    right = len(values) - 1

    while left <= right:
        middle = (left + right) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1
