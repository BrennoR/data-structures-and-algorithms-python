def insertion_sort(arr):
    for k in range(1, len(arr)):
        value = arr[k]
        position = k
        while position > 0 and arr[position - 1] > value:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = value

    return arr


test_arr = [1, 5, 2, 7, 48, 12, 443, 0, 3, 8, 4, 6]
print(insertion_sort(test_arr))
