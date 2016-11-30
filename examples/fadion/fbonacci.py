import math


def rec_fibonacci(x):
    if not isinstance(x, int) or x <= -1:
        return -1
    else:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            return rec_fibonacci(x - 1) + rec_fibonacci(x - 2)


def acc_fibonacci(x, a, b):
    if not isinstance(x, int) or x <= -1 or not isinstance(a, int) or a <= -1 or not isinstance(b, int) or b <= -1:
        return -1
    else:
        if x == 0:
            return a
        else:
            return acc_fibonacci(x - 1, a + b, a)


def iter_fibonacci(x):
    if not isinstance(x, int) or x <= -1:
        return -1
    else:
        a = 0
        b = 1
        for i in range(x):
            c = a + b
            a = b
            b = c
        return a


def list_fibonacci(x):
    if not isinstance(x, int) or x <= -1:
        return -1
    else:
        l = [0]
        if x > 0:
            l.append(1)
        for i in range(2, x + 1):
            l.append(l[-1] + l[-2])
        return l


# Binet's formula which we can derive from the generating function of the Fibonacci sequence
def root_fibonacci(x):
    if not isinstance(x, int) or x <= -1:
        return -1
    else:
        a = (1.0 + math.sqrt(5)) / 2.0
        b = (1.0 - math.sqrt(5)) / 2.0
        return (math.pow(a, x) - math.pow(b, x)) / math.sqrt(5)


print(rec_fibonacci(6))
print(acc_fibonacci(6, 0, 1))
print(iter_fibonacci(6))
print(list_fibonacci(6))
print(root_fibonacci(6))
