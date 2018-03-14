import math
def find_max_prime(target):
    i = 2
    primes = []
    while i < math.sqrt(target):
        while target % i == 0:
            target /= i
            primes.append(i)
            print primes
        i += 1
    primes.append(target)

    print primes
    print reduce(lambda x, y: x*y, primes)

print find_max_prime(600851475143)
