import itertools as it
import pprint, json, time

primes = []
prime_dict = {}

class ContinueI(Exception):
    pass

class ContinueJ(Exception):
    pass

class ContinueK(Exception):
    pass

class ContinueL(Exception):
    pass

def load_primes():
  try:
    with open('prime_dots.txt', 'r') as prime_file:
      result = prime_file.read()
    print("preloadPrimes loaded from file: ", len(result))
  except Exception as exc:
    print(exc)
    result = "  .. . .  "
    pass

  return list(result)

  # addPrimes(10000000)
  # print(len(primes))
  # print()
  # json.dump(primes, open('primes.json', 'w'))

def arePrimeCombos(primes, candidate, size):
  combinations = it.combinations(candidate, 2)
  # print("combinations: ", list(combinations))
  candidates = [(int(str(a) + str(b)),int(str(b) + str(a)))  for (a,b) in combinations]
  # candidates = [str(a) + str(b) for (a,b) in combinations]
  # print("candidates: ", candidates)
  candidates = list(it.chain.from_iterable(candidates))
  # print("candidates: ", candidates)
  # print("primes: ", len(primes))
  not_primes = [x for x in candidates if (x > len(primes)) or (primes[x] == ' ')]
  # print("not_primes: ", not_primes)
  # time.sleep(1)
  return len(not_primes) == 0

def isSafePrime(prime):
  return (str(prime).find('2') == -1) and (str(prime).find('5') == -1)

def main():
  primes = load_primes()
  index = 0
  max_prime = 100000000
  max_index = 100000
  primes = primes[:max_prime]
  print("Primes: ", len(primes))

  prime_dict = {index:True for index, value in enumerate(list(primes)) if value == '.'}
  print("Prime Dict: ", len(prime_dict))

  prime_keys = prime_dict.keys()
  print("Prime Keys: ", len(prime_keys))

  for x in range(10):
    print(x, prime_dict.get(x, False))

  results = []

  # for prime1 in [prime for prime in primes if (prime < max_prime) and isSafePrime(prime)]:
  # for prime1 in [index for index, value in enumerate(list(primes)) if (value == '.') and (index < max_index) and isSafePrime(index)]:
  for prime1 in [index for index in prime_keys if (index < max_index) and isSafePrime(index)]:
    candidate = [prime1]
    print("candidate: " + str(candidate))

    # for prime2 in [prime for prime in primes if (prime > prime1) and (prime < max_prime) and isSafePrime(prime)]:
    # for prime2 in [index for index, value in enumerate(list(primes)) if (value == '.') and (index > prime1) and (index < max_index) and isSafePrime(index)]:
    for prime2 in [index for index in prime_keys if (index > prime1) and (index < max_index) and isSafePrime(index)]:
      candidate2 = candidate + [prime2]
      try:
        if not arePrimeCombos(primes, candidate2, 2):
          raise ContinueI

        print("candidate2: " + str(candidate2))
        # for prime3 in [prime for prime in primes if (prime > prime2) and (prime < max_prime) and isSafePrime(prime)]:
        # for prime3 in [index for index, value in enumerate(list(primes)) if (value == '.') and (index > prime2) and (index < max_index) and isSafePrime(index)]:
        for prime3 in [index for index in prime_keys if (index > prime2) and (index < max_index) and isSafePrime(index)]:
          candidate3 = candidate2 + [prime3]
          try:
            if not arePrimeCombos(primes, candidate3, 3):
              raise ContinueJ

            print("candidate3: " + str(candidate3))
            # for prime4 in [prime for prime in primes if (prime > prime3) and (prime < max_prime) and isSafePrime(prime)]:
            # for prime4 in [index for index, value in enumerate(list(primes)) if (value == '.') and (index > prime3) and (index < max_index) and isSafePrime(index)]:
            for prime4 in [index for index in prime_keys if (index > prime3) and (index < max_index) and isSafePrime(index)]:
              candidate4 = candidate3 + [prime4]
              try:
                if not arePrimeCombos(primes, candidate4, 4):
                  raise ContinueK

                print("candidate4: " + str(candidate4))
                # for prime5 in [prime for prime in primes if (prime > prime4) and (prime < max_prime) and isSafePrime(prime)]:
                # for prime5 in [index for index, value in enumerate(list(primes)) if (value == '.') and (index > prime4) and (index < max_index) and isSafePrime(index)]:
                for prime5 in [index for index in prime_keys if (index > prime4) and (index < max_index) and isSafePrime(index)]:
                  candidate5 = candidate4 + [prime5]
                  try:
                    if not arePrimeCombos(primes, candidate5, 5):
                      raise ContinueL

                    print("candidate5: " + str(candidate5) + "   -   " + str(sum(candidate5)))
                    results.append(candidate5)
                    time.sleep(10)
                
                  except ContinueL:
                    continue

              except ContinueK:
                continue
            time.sleep(2)
        
          except ContinueJ:
            continue

      except ContinueI:
        continue

    pprint.pprint(results)
    pprint.pprint([sum(x) for x in results])

main()