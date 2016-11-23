def rec_factorial(x):
    if isinstance(x, int) and x > -1:
        if x == 0 or x == 1:
            return 1
        else:
            return x * rec_factorial(x - 1)
    else:
        return -1


def iter_factorial(x):
    if isinstance(x, int) and x > -1:
        a = 1
        for i in range(2, x):
            a *= i
        else:
            a *= x
        return a
    else:
        return -1


def list_factorial(x):
    if isinstance(x, int) and x > -1:
        l = [1]
        for i in range(1, x + 1):
            l.append(l[-1] * i)
        return l
    else:
        return -1


def acc_factorial(x, a):
    if isinstance(x, int) and x > -1 and isinstance(a, int) and a > 0:
        if x == 0 or x == 1:
            return a
        else:
            return acc_factorial(x - 1, a * x)
    else:
        return -1

print(rec_factorial(5))
print(iter_factorial(5))
print(list_factorial(5))
print(acc_factorial(5, 1))
