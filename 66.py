import math, pprint

def add_candidate_for_d(candidates, d):
  print("Testing {}".format(d))
  root_d = math.sqrt(d)
  if (root_d - int(root_d)) < 0.000001:
    return candidates
  x = 0
  while True:
    x = x + 1
    if x % 1000000 == 0:
      print("Testing x {}".format(x))
    if x % 100000000 == 0:
      return candidates

    y = int(math.sqrt(x*x/d))
    if y==0:
      continue
    remainder = (x*x) - (d*y*y)
    # if x % 10000 == 0:
      # print("{}^2 - {}*{}^2 = {}".format(x, d, y, remainder))
    if remainder == 1:
      candidates.append({"d": d, "x": x, "y": y})
      return candidates

def get_candidates():
  result = {}
  candidates = []
  for d in range(1001):
    candidates = add_candidate_for_d(candidates, d)
  return candidates

def get_answer(candidates):
  result = 0
  for candidate in candidates:
    if candidate['x'] > result:
      result = candidate['x']

  return result

def main():
  candidates = get_candidates()
  pprint.pprint(candidates)
  print("The result is: {}".format(get_answer(candidates)))

main()