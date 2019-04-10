def gap_insertion_sort(arr, start, gap):
    for i in range(start + gap, len(arr), gap):

        value = arr[i]
        pos = i

        while pos >= gap and arr[pos - gap] > value:
            arr[pos] = arr[pos - gap]
            pos -= gap

        arr[pos] = value

    return arr


def shell_sort(arr):
    sublist_count = len(arr) // 2
    while sublist_count > 0:

        for start_pos in range(sublist_count):
            gap_insertion_sort(arr, start_pos, sublist_count)

        print("After increments of size", sublist_count,
              "The list is", arr)

        sublist_count = sublist_count // 2

    return arr


test_arr = [1, 5, 2, 7, 48, 12, 443, 0, 3, 8, 4, 6]
shell_sort(test_arr)
