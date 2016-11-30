def rec_factorial(x):
    if not isinstance(x, int) or x <= -1:
        return -1
    else:
        if x == 0 or x == 1:
            return 1
        else:
            return x * rec_factorial(x - 1)


def iter_factorial(x):
    if not isinstance(x, int) or x <= -1:
        return -1
    else:
        a = 1
        for i in range(2, x):
            a *= i
        else:
            a *= x
        return a


def list_factorial(x):
    if not isinstance(x, int) or x <= -1:
        return -1
    else:
        l = [1]
        for i in range(1, x + 1):
            l.append(l[-1] * i)
        return l


def acc_factorial(x, a):
    if not isinstance(x, int) or x <= -1 or not isinstance(a, int) or a <= 0:
        return -1
    else:
        if x == 0 or x == 1:
            return a
        else:
            return acc_factorial(x - 1, a * x)


print(rec_factorial(5))
print(iter_factorial(5))
print(list_factorial(5))
print(acc_factorial(5, 1))
