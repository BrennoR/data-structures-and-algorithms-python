def binary_search(input_array, value):
    """ Performs a binary search for a value in a list"""
    low = 0
    high = len(input_array) - 1

    while low <= high:
        mid = (low + high) // 2
        if input_array[mid] == value:
            return mid
        elif input_array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1
