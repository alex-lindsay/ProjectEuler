import math
solutions = [2]

primes = [2]

def is_prime(num):
    if num in primes:
        return True
    for prime in primes:
        if num % prime == 0:
            return False
        if prime > math.sqrt(num):
            primes.append(num)
            return True

    primes.append(num)
    return True

def check_rotations(num):
    test = str(num)
    if len(test) == 1:
        return True
    for _ in range(1, len(test)):
        test = test[1:] + test[0]
        if not is_prime(int(test)):
            return False
    
    return True

def add_solutions(num):
    test = str(num)
    for _ in range(0, len(test)):
        solutions.append(int(test))
        test = test[1:] + test[0]


# for a in range(3, 100, 2):
for a in range(3, 1000000, 2):
    # if a in solutions:
    #     print(a,"already found")
    #     continue
    if a % 10000 == 1:
        print(a, "reviewed")
    is_prime(a)
    
for prime in primes:
    if check_rotations(prime):
        add_solutions(prime)

solutions = sorted(list(set(solutions)))

print(primes[:10])
print(primes[-10:])
print(len(primes))

print(solutions)
print(solutions[:10])
print("Result:", len(solutions))