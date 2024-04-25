def prime_numbers_before(n):
    primes = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


print(prime_numbers_before(200))
