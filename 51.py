import itertools, time

prime_limit = 1000000
# prime_limit = 100000
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
for num in range(2, prime_limit):
    if num % 100000 == 0:
        print(num)
    is_prime(num)

print("Primes assembled")

def test_prime(prime):
    s_prime = list(str(prime))
    s_len = len(s_prime)
    if (prime % 10000 == 1):
        print(prime, s_len)
    for i in range(2, 2**s_len, 2):
        s_i_bin = format(i, "#0" + str(s_len+2) + 'b')[2:]
        family_pattern = [digit == '1' for digit in list(s_i_bin)]
        # print(s_i_bin, family_pattern)
        family = [int("".join([swap and str(sub) or s_prime[idx] for idx, swap in enumerate(family_pattern) ])) for sub in range(0, 10)]
        # print(family)
        prime_family = [num for num in family if is_prime(num)]
        if len(prime_family) > 6:
            print(prime, i, s_i_bin, prime_family)
            print()
            if len(prime_family) >= 8:
                print("^" * 50)
                print()
                return True
    return False

for prime in primes:
    if prime < 56003:
        continue

    # if prime > 56010:
    #     break
    
    if test_prime(prime):
        # break
        pass