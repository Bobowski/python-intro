def rec_fibonacci(n):
    if not isinstance(n, int):
        return -1
    if n == 0 or n == 1:
        return 1
    else:
        return rec_fibonacci(n-1)+rec_fibonacci(n-2)


def iter_fibonacci(n):
    if not isinstance(n, int):
        return -1
    if n == 0 or n == 1:
        return 1
    else:
        a, b = 1, 1
        for i in range(2, n+1):
            c = a + b
            a = b
            b =c
        return c


print(rec_fibonacci(4))
print(iter_fibonacci(5))