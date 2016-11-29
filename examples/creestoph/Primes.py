import math
import random


def is_prime(n):
    if not isinstance(n, int) or n <= 1:
        return -1
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def erastotenes(n):
    if not isinstance(n, int) or n < 0:
        return -1
    tab = []
    res = []
    sqrt = int(math.sqrt(n))
    for i in range(n):
        tab.append(True)
    for i in range(2, sqrt):
        if tab[i]:
            for j in range(i * i, n, i):
                tab[j] = False
    for i in range(2, n):
        if tab[i]:
            res.append(i)
    return res


def only_primes(tab):
    return list(filter(is_prime, tab))


def power_modulo_fast(a, b, m):
    i = 1
    result = 1
    x = a % m
    while i <= b:
        x %= m
        if b & i != 0:
            result *= x
            result %= m
        x *= x
        i <<= 1
    return result


def miller_rabin_test(n, k):
    if not isinstance(n, int) or n <= 1 or not isinstance(k, int) or k < 0:
        return -1
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d /= 2
        s += 1
    for i in range(k):
        a = random.randint(1, n - 1)
        if power_modulo_fast(a, int(d), n) != 1:
            complex = True
            for r in range(s):
                if power_modulo_fast(a, int((2 ** r) * d), n) == n - 1:
                    complex = False
                    break
            if complex:
                return False
    return True


open("primes.txt", 'w').write(
    "\n".join(map(str, erastotenes(135999899))))  # biggest int, that doesn't cause memory error
