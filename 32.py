solutions = []
total = 0

for a in range(1,10000):
    if a % 100 == 0:
        print("a", a)
    for b in range(a,10000):
        c = a * b
        s = "".join(sorted(list(str(c) + str(a) + str(b))))
        if s == "123456789":
            print(a, b, c)
            solutions.append((a, b, c))

totals = set([c for (a,b,c) in solutions])

print(totals)

print(sum(totals))