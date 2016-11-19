import math


def rec_factorial(a):
    if not isinstance(a, int):
        return 0
    elif a > 1:
        return a * rec_factorial(a - 1)
    else:
        return 1


def iter_factorial(a):
    if not isinstance(a, int):
        return 0
    b = 1
    for i in range(2, a + 1):
        b *= i
    return b


def list_factorial(n):
    if not isinstance(n, int):
        return 0
    fact = []
    for i in range(0, n):
        fact.append(math.factorial(i))
    return fact


print(list_factorial(10))
