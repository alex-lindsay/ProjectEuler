import math, json

primes = [2, 3]
corners = [1]
cornerPrimes = []

def isPrime(aNumber):
    global primes
    # print(aNumber, primes[aNumber])
    return primes[aNumber] == "."
    # return prime_dict.get(aNumber, False)


def addCorners():
    global corners, cornerPrimes
    layers = int(len(corners) / 4)
    maxCorner = (layers > 0) and corners[-1] or 1
    newCorners = [int(maxCorner + (2 * (layers+1) * index)) for index in range(1, 5)]
    corners.extend(newCorners)
    # addPrimes(corners[-1])
    print(newCorners, [corner for corner in newCorners if isPrime(corner)])
    cornerPrimes.extend([corner for corner in newCorners if isPrime(corner)])


def done():
    global corners, cornerPrimes
    side = int((len(corners) + 1) / 2)
    if (side == 1):
        return False
    # print("side: " + str(side))
    result = (side > 50000)
    # print("len(corners): " + str(len(corners)))
    # print("(len(cornerPrimes) / (len(corners)): " + str((len(cornerPrimes) / (len(corners)))))
    result = result or ((len(corners) > 3) and ((len(cornerPrimes) / len(corners)) < 0.1))
    return result


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
    global primes
    primes = load_primes()
    while not done():
        addCorners()
        # print("layers:", int(len(corners) / 4))
        # print("corners:", corners)
        # print("primes:", primes)
        # print("corner primes:", cornerPrimes)
        print("SideLength:", ((len(corners) + 1) / 2), len(cornerPrimes), len(corners), len(cornerPrimes) / len(corners))
        # print()

    print(len(primes))
    # print(cornerPrimes[-1], corners[-1], primes[-1])


main()