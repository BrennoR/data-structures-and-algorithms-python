# bubble sort with all passes
def bubble_sort(arr):
    count = 0
    for n in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        count += 1

    print("Full bubble sort:", count)
    return arr


# bubble sort with early stopping
def bubble_sort_short(arr):
    sorted = False
    count = 0
    while not sorted:
        sorted = True
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                sorted = False
        count += 1

    print("Short bubble sort:", count)

    return arr


test_arr = [1, 5, 2, 7, 48, 12, 443, 0, 3, 8, 4, 6]
# print(bubble_sort(test_arr))
print(bubble_sort_short(test_arr))
