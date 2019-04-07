def get_fib(position):
    """ Gets the fibonacci sequence value at the desired position """
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)


def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])


print(listsum([1, 3, 5, 7, 9]))


def to_str(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return to_str(n // base, base) + convertString[n % base]


print(to_str(10, 2))


def reverse_str(string):
    if len(string) == 1:
        return string[0]
    else:
        return reverse_str(string[1:]) + string[0]


print(reverse_str("hello"))
