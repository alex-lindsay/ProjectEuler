import math
from fractions import gcd

# a are the leading integers
# b is the numerator passed in
# c is the root started with
# d is the additive with the root
def get_values(indexes, s, b, c, d):
  den  = c - (d*d)
  print({'indexes': indexes, "expr": "{}/(√{} {})".format(b, c, d)})
  if den == 0:
    result = (indexes, 0, 0, 0)
  else:
    print({"intermediate": ">>", "expr": "{}(√{} + {}) / {}".format(b, c, -d, den)})
    val = b * (s - d) / den
    aa = int(val)
    bb = 1
    cc = - (b * d) - (aa * den)
    dd = den

    fac = int(gcd(cc, dd))
    cc = int(cc / fac)
    dd = int(dd / fac)

    result = (indexes + [aa], dd, bb, cc)
    print({"output": ">>", "expr": "{} + (√{} {}) / {}".format(aa, c, cc, dd), "fac": fac}, end="\n\n")
  return result
    

def get_order(indexes):
  if all([elem == 0 for elem in indexes]):
    return 0
  for n in range(1, len(indexes)+1):
    test = [indexes[i*n:((i+1)*n)] for i in range(0, (len(indexes) // n) + 1)]
    # print(test)
    if all([elem == test[0] for elem in test[:-1]]):
      return n

  return len(indexes)

def main():
  result = 0
  for n in range(1, 8):
    print("STARTING ", n)
    indexes = []
    s = math.sqrt(n)
    a = int(s)
    b = 1
    c = n
    d = -a
    for i in range(1, (2*n)+1):
      (indexes, b, c, d) = get_values(indexes, s, b, n, d)

    print(n, indexes)
    print()
    root_order = get_order(indexes)
    print("The root order of {} is {}".format(n, root_order), end="\n\n")


main()