import itertools, time

primes = []

def is_prime(num):
    if num < 2:
        return False
    if num in primes:
        return True
    for prime in primes:
        if num % prime == 0:
            return False
    primes.append(num)
    return True

for num in range(2, 10000):
    is_prime(num)

for p0 in [p for p in primes if p >= 1000]:
    perms = set([int(''.join(perm)) for perm in list(itertools.permutations(list(str(p0))))])
    # print(perms)
    p_perms = sorted([p_perm for p_perm in perms if (p_perm >= 1000) and is_prime(p_perm)])
    if len(p_perms) >= 3:
        # print(p_perms)
        diffs = [[p_perms[b] - p_perms[a] for b in range(0, len(p_perms))] for a in range(0, len(p_perms))]
        # print(diffs)
        rediffs = [[(ia, ib, b) for (ib, b) in enumerate(a) if (b != 0) and (b in diffs[ib])] for (ia, a) in enumerate(diffs)]
        if any([len(v) > 0 for v in rediffs]):
            print(p0, rediffs)
        # print()