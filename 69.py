import pprint, math, json

def load_primes():
  with open("primes.json", "r") as pfile:
    result = json.load(pfile)
  return result

def setup_working_data(stop):
  working_data = {n:0 for n in range(2, stop+1)}
  return working_data

# Count the number of distinct prime factors each number has.
# The more prime factors, the fewer relative primes it can have
def process_primes(stop, primes, working_data):
  for prime in primes:
    if prime > stop:
      break
    for n in range(prime, stop+1, prime):
      working_data[n] = working_data[n] + 1

  return working_data

def main():
  stop = 100
  primes = load_primes()

  working_data = setup_working_data(stop)

  working_data = process_primes(stop, primes, working_data)
  pprint.pprint(working_data)

  result = 0
  print("The value is highest for n = {}".format(result))

main()