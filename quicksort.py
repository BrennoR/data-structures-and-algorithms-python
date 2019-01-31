def quicksort(array):
    """ Quicksort algorithm """
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x > pivot:
                greater.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                less.append(x)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return array
