import pprint, itertools

def figurate(min, max, func):
  result = []
  index = 0
  while True:
    # triangle = int(index * (index + 1) / 2)
    value = func(index)
    if value > max:
      break
    elif value > min:
      result.append(str(value))
    index = index + 1
  return result

def triangles(min, max):
  return figurate(min, max, lambda n: int(n * (n + 1) / 2))

def squares(min, max):
  return figurate(min, max, lambda n: int(n * n))

def pentagons(min, max):
  return figurate(min, max, lambda n: int(n * (3 * n - 1) / 2))

def hexagons(min, max):
  return figurate(min, max, lambda n: int(n * (2 * n - 1)))

def heptagons(min, max):
  return figurate(min, max, lambda n: int(n * (5 * n - 3) / 2))

def octagons(min, max):
  return figurate(min, max, lambda n: int(n * (3 * n - 2)))

def main():
  min = 1000
  max = 10000
  figurates = {
    3: triangles(min, max),
    4: squares(min, max),
    5: pentagons(min, max),
    6: hexagons(min, max),
    7: heptagons(min, max),
    8: octagons(min, max)
  }

  tests = itertools.permutations(range(3, 9), 6)
  for test in tests:
    keys = list(test)
    candidates = []
    candidates.append(figurates[test[0]])
    candidates.append([[candidate, candidate1] for candidate1 in figurates[keys[1]] for candidate in candidates[-1] if candidate1[:2] == candidate[2:]])
    candidates.append([candidate + [candidate2] for candidate2 in figurates[keys[2]] for candidate in candidates[-1] if candidate2[:2] == candidate[-1][2:]])
    candidates.append([candidate + [candidate3] for candidate3 in figurates[keys[3]] for candidate in candidates[-1] if candidate3[:2] == candidate[-1][2:]])
    candidates.append([candidate + [candidate4] for candidate4 in figurates[keys[4]] for candidate in candidates[-1] if candidate4[:2] == candidate[-1][2:]])
    candidates.append([candidate + [candidate5] for candidate5 in figurates[keys[5]] for candidate in candidates[-1] if (candidate5[:2] == candidate[-1][2:]) and (candidate[0][:2] == candidate5[2:])])

    if (len(candidates[-1]) > 0):
      print(keys)
      for candidate in candidates[-1]:
        print(candidate, [sum([int(x) for x in candidate]) for candidate in candidates[-1]])

  # pprint.pprint({index: " ".join(value) for index, value in figurates.items()})


main()