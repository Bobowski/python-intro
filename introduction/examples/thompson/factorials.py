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
    while a > 1:
        b *= a
        a -= 1
    return b


# def iter_factorial(a):
#     if not isinstance(a, int):
#         return 0
#     b = 1
#     for i in range(a + 1):
#         if i != 0:
#             b = b * i
#     return b


def list_factorial(n):
    if not isinstance(n, int):
        return 0
    list = []
    i = 1
    while i <= n:
        list.append(math.factorial(i))
        i += 1
    return list