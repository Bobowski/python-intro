def list_fibonacci(n):
    if not isinstance(n, int):
        return 0
    if n >= 0:
        list1 = []
        pre = 0
        post = 1
        for i in range(n):
            pre, post = post, pre + post
            list1.append(pre)
        return list1
    return 0


def iter_fibonacci(n):
    if isinstance(n, int):
        pre = 0
        post = 1
        for i in range(n):
            pre, post = post, pre + post
        return pre
    else:
        return 0


def rec_fibonacci(n):
    if n in [0, 1]:
        return n
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
