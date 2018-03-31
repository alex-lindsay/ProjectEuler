import time
def triangular_number(n):
    return (n * (n + 1)) / 2

def pentagonal_number(n):
    return (n * ((3 * n) - 1)) / 2

def hexagonal_number(n):
    return n * ((2 * n) - 1)

t = 286
p = 165
h = 143

# t = 2
# p = 2
# h = 2

while True:
    while (triangular_number(t) < pentagonal_number(p)) or \
        (triangular_number(t) < hexagonal_number(h)):
        t += 1
    if t%100 == 0:
        print("Testing t,p,h:", t, p, h)

    while (pentagonal_number(p) < triangular_number(t)):
        p += 1

    while (hexagonal_number(h) < triangular_number(t)):
        h += 1

    if (triangular_number(t) == pentagonal_number(p)):
        print("Triangle #", t, "is also Pentagonal #", p, "=>", triangular_number(t))
        time.sleep(2)

    # if (triangular_number(t) == hexagonal_number(h)):
    #     print("Triangle #", t, "is also Hexagonal #", h, "=>", triangular_number(t))
    #     time.sleep(2)

    if (triangular_number(t) == pentagonal_number(p)) and \
        (triangular_number(t) == hexagonal_number(h)):
        print("Solution: T:", t, "P:", p, "H:", h, "=>", triangular_number(t))
        break

    t += 1
