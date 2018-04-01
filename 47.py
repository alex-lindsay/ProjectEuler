import math

primes = [2]

def is_prime(num):
    if num in primes:
        return True
    for prime in [p for p in primes if p < math.sqrt(num)]:
        if num % prime == 0:
            return False

    primes.append(num)
    return True

def prime_factors(num):
    result = []
    for prime in primes:
        if num == 1:
            return result
        while num % prime == 0:
            result.append(prime)
            num /= prime
    return result

def has_four_distinct_factors(num):
    test = prime_factors(num)
    stest = set(test)
    return (len(stest) == 4)

i = 2
max_len = 0
solutions = []
while (i<1000000000) and (len(solutions) < 4):
    if i % 10000 == 0:
        print(i)
    if not is_prime(i):
        if has_four_distinct_factors(i):
            solutions.append((i, prime_factors(i)))
            if len(solutions) > max_len:
                print(solutions)
                max_len = len(solutions)
        else:
            solutions = []
    else:
        solutions = []
    i += 1

print(solutions)