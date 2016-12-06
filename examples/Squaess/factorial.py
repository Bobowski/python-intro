def rec_factorial(n):
    if not isinstance(n, int):
        return -1
    if n < 0:
        return -1
    if n == 0 or n == 1:
        return 1
    else:
        return n*rec_factorial(n-1)


def iter_factorial(n):
    if not isinstance(n, int):
        return -1
    elif n <= -1:
        return -1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result


def list_factorial(n):
    if not isinstance(n, int):
        return -1
    else:
        list = [1]
        for i in range(1, n+1):
            list.append(list[-1]*i)
        return list


def acc_factorial(n, acc):
    if not isinstance(n, int):
        return -1
    if n < 0:
        return -1
    if n == 0 or n == 1:
        return acc
    else:
        return acc_factorial(n-1, acc*n)


def wrp_acc_factorial(n):
    return acc_factorial(n, 1)

print(rec_factorial(3))
print(iter_factorial(3))
print(list_factorial(3))
print(wrp_acc_factorial(3))