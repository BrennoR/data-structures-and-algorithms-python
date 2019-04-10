def selection_sort(arr):
    for k in range(len(arr) - 1, 0, -1):
        max_idx = 0
        for j in range(1, k + 1):
            if arr[j] > arr[max_idx]:
                max_idx = j

        temp = arr[max_idx]
        arr[max_idx] = arr[k]
        arr[k] = temp

    return arr


test_arr = [1, 5, 2, 7, 48, 12, 443, 0, 3, 8, 4, 6]
print(selection_sort(test_arr))

