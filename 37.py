import math
solutions = []

primes = []

def is_prime(num):
    if num == 1:
        return False
    if num in primes:
        return True
    for prime in primes:
        if prime > math.sqrt(num):
            primes.append(num)
            return True
        if num % prime == 0:
            return False
    primes.append(num)
    return True

def truncations_are_prime(num):
    for i in range(1, len(str(num))):
        if not is_prime(int(str(num)[i:])):
            return False
        if not is_prime(int(str(num)[:-i])):
            return False
    print(num, "is a solution!")
    return True

a = 2
while (len(solutions) < 11) and (a < 1000000):
    if is_prime(a):
        # print(a, "is prime")
        if a >= 10:
            if truncations_are_prime(a):
                solutions.append(a)

    a += 1

print(primes)
print(solutions)
print("Result:", sum(solutions))