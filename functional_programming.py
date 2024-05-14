

def fibonacci(n: int) -> int:
    """
    Computes the nth Fibonacci number.
    :param n: The index of the Fibonacci number to compute.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def add_number(num: int) -> callable:
    """
    Creates a function that adds num to a given number.
    :param num: The number to add.
    """
    def add(x: int) -> int:
        return x + num
    return add


def fibonacci_plus_n(n: int, num: int) -> int:
    """
    Computes the nth Fibonacci number and adds num to it.
    :param n: The index of the Fibonacci number to compute.
    :param num: The number to add to the Fibonacci number.
    """
    return add_number(num)(fibonacci(n))
