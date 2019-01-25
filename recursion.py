def get_fib(position):
    """ Gets the fibonacci sequence value at the desired position """
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)
