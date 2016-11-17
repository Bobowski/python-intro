import math


def is_prime(n):
    if isinstance(n, int):
        if n <= 0:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, math.floor(math.sqrt(n)), 2):
            if n % i == 0:
                return False
        return True
    return False
