# uUse Sieve of Eratosthenes for checking the prime

def countPrimes(n):
    if n < 2: return 0

    primes = [True for i in range(n)]
    # primes = [True] * n (can use instead)
    primes[0] = primes[1] = False

    for p in range(2, int(n**0.5)+1): # Optimal: up to sqrt(n)
        if primes[p]:
            for i in range(p * p, n, p): # Optimal: start from p*p
                primes[i] = False

        return sum(primes)


print(countPrimes(10))