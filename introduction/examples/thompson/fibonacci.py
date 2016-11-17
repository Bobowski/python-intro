def list_fibonacci(n):
    if isinstance(n, int):
        if n >= 0:
            list1 = [0]
            pre = 0
            post = 1
            for i in range(n):
                tmp = pre + post
                pre = post
                post = tmp
                list1.append(pre)
            return list1
        return 0
    return 0


def iter_fibonacii(n):
    if isinstance(n, int):
        pre = 0
        post = 1
        for i in range(n):
            tmp = pre + post
            pre, post = post, tmp
        return pre
    else:
        return 0


def rec_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec_fibonacci(n - 1) + rec_fibonacci(n - 2)


def acc_fibonacci(n):
    def acc(m, a1, a2):
        if m == 0:
            return a2
        else:
            return acc(m - 1, a2, a1 + a2)

    if n == 0:
        return 1
    else:
        return acc(n - 1, 1, 1)
