# Example solutions to Fibonacci exercises
# Many thanks to Krzysiek Strzelecki for those solutions
# I did some code formatting to make it a bit more readable (PEP8)


def rec_fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return rec_fibonacci(n - 2) + rec_fibonacci(n - 1)


# [Adam] Some explanation will be needed here (tail recursion)
# TODO Explain tail recursion :D

def acc_fibonacci(n, a, b):
    if n == 0:
        return a
    else:
        return acc_fibonacci(n - 1, a + b, a)


def iter_fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c
    return a


# [Adam] We can use Python unpacking to use fewer lines :D
def iter_fibonacci2(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def list_fibonacci(n):
    res = [0]
    if n > 0:
        res.append(1)
    for i in range(2, n + 1):
        res.append(res[i - 1] + res[i - 2])
    return res
