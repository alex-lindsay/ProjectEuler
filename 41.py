import math
solutions = []
digits = "123456789"

#there are no 9 digit pandigital primes.  multiple of 9
endAt = 100000000

def sieve_of_eratosthenes():
    print("Initializing sieve list")
    ptracker = [True for n in range(0,endAt)]
    ptracker[0] = False
    ptracker[1] = False
    print("Sieve initialized")
    for i in range(2, int(math.sqrt(endAt))):
        if i % 100 == 0:
            print("Sieve testing", i)
        if ptracker[i]:
            j = i ** 2
            while j < endAt:
                ptracker[j] = False
                j += i
    print(ptracker[:20])
    print(ptracker[-20:])
    print("Done testing primes")
    return [index for (index, value) in enumerate(ptracker) if value == True]


def is_prime(num):
    if num < 2:
        return False
    if num in primes:
        return True
    for prime in primes:
        if prime > math.sqrt(num):
            break
        if num % prime == 0:
            return False
    # print(num, prime)
    primes.append(num)
    return True

def is_pandigital(num):
    s = str(num)
    #no pandigital number can contain a 0
    if "0" in str(prime):
        return False
    # print(num, "".join(sorted(set(list(s)))), digits[0:len(s)])
    return "".join(sorted(set(list(s)))) == digits[0:len(s)]

primes = sieve_of_eratosthenes()
print(primes[:20])
print(primes[-20:])
print(len(primes))

for prime in primes:
    # print("Checking", prime)
    if is_pandigital(prime):
        print(prime)
        solutions.append(prime)

print(solutions)
print("Result:", max(solutions))