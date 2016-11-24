import math


def rec_fibonacci(n):
    if not isinstance(n, int) or n < 0:
        return -1
    if n == 0 or n == 1:
        return n
    else:
        return rec_fibonacci(n-2) + rec_fibonacci(n-1)


def acc_fibonacci(n, a, b):
    if not isinstance(n, int) or n < 0 or not isinstance(a, int) or a < 0 or not isinstance(b, int) or b < 0:
        return -1
    if n == 0:
        return a
    else:
        return acc_fibonacci(n-1, a+b, a)


def iter_fibonacci(n):
    if not isinstance(n, int) or n < 0:
        return -1
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c
    return a


def list_fibonacci(n):
    if not isinstance(n, int) or n < 0:
        return -1
    res = [0]
    if n > 0:
        res.append(1)
    for i in range(2, n+1):
        res.append(res[i-1]+res[i-2])
    return res


def root_factorial(n):
    if not isinstance(n, int) or n < 0:
        return -1
    s5 = math.sqrt(5)
    return (((1+s5)/2)**n)/s5


def check_delta(delta):
    if not isinstance(delta, float) or delta < 0:
        return -1
    d = delta + 1
    n = 0
    while d > delta:
        d = math.fabs(root_factorial(n) - iter_fibonacci(n))
        n += 1
    return list(range(n))

print(list_fibonacci(13))
print(check_delta(0.01))