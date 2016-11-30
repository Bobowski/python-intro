import math
import random


def is_prime(x):
    if not isinstance(x, int):
        return False
    elif x <= 1:
        return False
    else:
        if x == 2:
            return True
        elif x % 2 == 0:
            return False
        else:
            i = 3
            while i <= math.sqrt(x):
                if x % i == 0:
                    return False
                i += 2
            return True


def eratosthenes(x):
    if not isinstance(x, int):
        return False
    elif x <= 1:
        return False
    else:
        numbers = [False, False]
        primes = []
        for i in range(x):
            numbers.append(True)
        i = 2
        while i <= x:
            numbers[i] = False
            i += 2
        i = 3
        while i * i <= x:
            if numbers[i]:
                j = i + i
                while j <= x:
                    numbers[j] = False
                    j = j + i
            i += 2
        primes.append(2)
        i = 3
        while i <= x:
            if numbers[i]:
                primes.append(i)
            i += 2
        return primes


def only_primes(x):
    if not isinstance(x, list):
        return -1
    else:
        i = 0
        y = []
        for r in map(is_prime, x):
            if r:
                y.append(x[i])
            i += 1
        return y


def miller_rabin_test(x, y):
    if not isinstance(x, int):
        return False
    elif x <= 1:
        return False
    elif not isinstance(y, int):
        return False
    elif y <= 0:
        return False
    else:
        if x == 2:
            return True
        elif x % 2 == 0:
            return False
        else:
            s = 0
            d = x - 1
            while d % 2 == 0:
                s += 1
                d //= 2
            for _ in range(y):
                a = random.randrange(1, x - 1)
                z = pow(a, d, x)
                if z == 1 or z == x - 1:
                    continue
                for i in range(s - 1):
                    z = pow(z, 2, x)
                    if z == x - 1:
                        break
                else:
                    return False
        return True


print(is_prime(19))
print(eratosthenes(20))
print(only_primes([1, 2, 6, 7]))
print(miller_rabin_test(223, 40))
