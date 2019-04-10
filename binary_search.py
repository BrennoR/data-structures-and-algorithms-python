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


def binary_search_rec(input_array, value):
    low = 0
    high = len(input_array) - 1

    def binary_rec(low, high):
        mid = (low + high) // 2
        if low > high:
            return -1
        elif input_array[mid] > value:
            return binary_rec(low, mid - 1)
        elif input_array[mid] < value:
            return binary_rec(mid + 1, high)
        else:
            return mid

    return binary_rec(low, high)


arr = [1, 3, 5, 6, 7, 10, 15]
print(binary_search(arr, 5))
print(binary_search_rec(arr, 5))
