def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)

    return arr


def quick_sort_helper(arr, first, last):
    if first < last:

        splitpoint = partition(arr, first, last)

        quick_sort_helper(arr, first, splitpoint - 1)
        quick_sort_helper(arr, splitpoint + 1, last)


def partition(arr, first, last):
    pivot = arr[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivot:
            leftmark += 1

        while arr[rightmark] >= pivot and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark


test_arr = [1, 5, 2, 7, 48, 12, 443, 0, 3, 8, 4, 6]
print(quick_sort(test_arr))
