# Function returns a list of prime numbers from 2 to n
def eratosthenes(n):
    if not isinstance(n, int):
        return 0
    if n >= 2:
        numbers = [False, False]
        primes = []
        i = n - 1
        for k in range(i):
            numbers.append(True)
        # while i:
        #     numbers.append(True)
        #     i -= 1
        z = 2
        while z <= n:
            numbers[z] = False
            z *= 2
        j = 3
        while j * j <= n:
            if not numbers[j]:
                j += 2
            else:
                k = j + j
                while k <= n:
                    numbers[k] = False
                    k += j
                j += 2
        primes.append(2)
        x = 3
        while x <= n:
            if numbers[x]:
                primes.append(x)
            x += 2
        return primes
    return 0