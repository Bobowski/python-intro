# Example solutions to Factorial exercises
# Many thanks to Krzysiek Strzelecki for those solutions
# I did some code formatting to make it a bit more readable (PEP8)


def rec_factorial(n):
    if not isinstance(n, int) or n < 0:
        return -1
    if n == 0 or n == 1:
        return 1
    else:
        return n * rec_factorial(n - 1)


def iter_factorial(n):
    if not isinstance(n, int) or n < 0:
        return -1
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def list_factorial(n):
    if not isinstance(n, int) or n < 0:
        return -1
    res = [1]
    for i in range(1, n + 1):
        res.append(res[-1] * i)
    return res


def acc_factorial(n, acc):
    if not isinstance(n, int) or n < 0:
        return -1
    if not isinstance(acc, int) or acc < 0:
        return -1
    if n == 0 or n == 1:
        return acc
    else:
        return acc_factorial(n - 1, acc * n)


# Functions with accumulators should be wrapped
# in other function to set initial value of acc
# So that function arguments are the same for each function

def wrp_acc_factorial(n):
    return acc_factorial(n, 1)
