#!/usr/bin/env python3

def fibonacci(n):
    """ 
        :param n: nth Fibonnaci number

        Based on the definition of the Fibonacci formula,
        if the Fibonacci of n == 0, the function should return,  0
        if the Fibonacci of n == 1, the function should return,  1

    """
    if n == 0:
        return 0 
    if n == 1:
        return 1
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """ 
        :param: n, nth Lucas number

        Based on the definition of a lucas formula,
        if the lucas of n == 0, the function should return, 2
        if the lucas of n == 1, the function should return, 1

    """
    if n == 0: 
        return 2 
    if n == 1: 
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, n0=0, n1=1):
    """
    :param n: nth value of a summation series. 
    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series

    """

    if n0 == 0 and n1 == 1: 
        return fibonacci(n)
    elif n0 == 2 and n1 == 1: 
        return lucas(n)
    else: 
        if n == 0:
            return 3
        if n == 1: 
            return 2
        else:
            return sum_series(n-1, n0, n1) + sum_series(n-2, n0, n1)

if __name__ == "__main__":
    # run some tests

    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13


    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7

    
    # test that sum_series matches fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)


    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")

