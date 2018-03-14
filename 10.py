primes = [2]

def isPrime(a):
    for prime in primes:
        if a % prime == 0:
            return False
    return True

a = 3
while a<2000000:
    if a%100000==1:
        print("Checking ", a)
    if isPrime(a):
        primes.append(a)

    a += 2

print(primes)
print(sum(primes))