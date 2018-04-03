import itertools, time

primes = [2]

def is_prime(num):
    if num < 2:
        return False
    if (num < primes[-1]) and (num in primes):
        return True
    for prime in primes:
        if num % prime == 0:
            return False
    primes.append(num)
    return True

print("Assembling primes")
for num in range(2, 1000000):
    if num % 100000 == 0:
        print(num)
    is_prime(num)

print("Primes assembled")

def test_range_sum(num_primes):
    for a in range(0, len(primes)-num_primes):
        test = sum(primes[a:a+num_primes])
        if test > 1000000:
            return False
        if is_prime(test):
            print(a, test, num_primes)
            return True


num_primes = len(primes)
while True:
    print("Number of primes:", num_primes)
    if test_range_sum(num_primes):
        break
    num_primes -= 1            

