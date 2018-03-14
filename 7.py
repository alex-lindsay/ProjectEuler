primes = [2]
i = 3
while len(primes) < 10001:
    isPrime = True
    for prime in primes:
        if i % prime == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(i)
        if len(primes) % 10 == 0:
            print (str(len(primes)) + " primes found")
    i += 2

print(primes[-5:])