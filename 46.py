import math

primes = [2]

def is_prime(num):
    if num in primes:
        return True
    for prime in [i for i in primes if i < math.sqrt(num)+1]:
        if num % prime == 0:
            return False

    primes.append(num)
    # print(primes)
    return True

def test_conjecture(num):
    for s in range (1, num):
        p = num - 2 * (s**2)
        if (p>0) and is_prime(p):
            print(num, p, s)
            return True
    return False


i = 3
keep_going = True
while keep_going:
    if (not is_prime(i)):
        # print("Testing", i, int(math.sqrt(i)/2))
        if not test_conjecture(i):
            print("Result:", i)
            break
    i += 2
    keep_going = (i<10000)