import sys, itertools as it

def extend_primes(primes, max_integer):
  curr_max = len(primes)
  primes = primes + list(it.repeat(".", (max_integer - len(primes))))
  next_prime = 2
  try:
    while next_prime < curr_max:
      for index in range(2*next_prime, max_integer, next_prime):
        primes[index] = ' '
      next_prime = primes.index('.', next_prime+1)
  except ValueError:
    pass

  with open('prime_dots.txt', 'w') as prime_file:
    prime_file.write(''.join(primes))

  return primes

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

def main():
  primes = load_primes()
  # print(primes)
  max_integer = (len(sys.argv) > 1) and int(sys.argv[1]) or ((len(primes) > 1000) and (len(primes) * 2) or 1000)
  primes = extend_primes(primes, max_integer)

  # print(primes)
  # print([index for index, value in enumerate(list(primes)) if value == '.'])

main()