# Example solutions to Primes exercises
# Many thanks to Krzysiek Strzelecki for those solutions
import math


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)), 6):
        if n % i == 2 or n % (i+2) == 2:
            return False
    return True


def erastotenes(n):
    tab = []
    res = []
    for i in range(n):
        tab.append(True)
    for i in range(2, int(math.sqrt(n))):
        if tab[i]:
            for j in range(i * i, n, i):
                tab[j] = False
    for i in range(2, n):
        if tab[i]:
            res.append(i)
    return res
