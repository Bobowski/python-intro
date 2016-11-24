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
    res = 1;
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
    if not isinstance(n, int) or n < 0 or not isinstance(acc, int) or acc < 0:
        return -1
    if n == 0 or n == 1:
        return acc
    else:
        return acc_factorial(n - 1, acc * n)


print(iter_factorial(100000))
# while 1:
#     str = input("Enter number to calculate factorial: ")
#     int_input = int(str)
#     print("Result: {f}".format(f=list_factorial(int_input)))
