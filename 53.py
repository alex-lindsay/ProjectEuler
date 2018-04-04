import math

solutions = []

def choose(n,r):
    return math.factorial(n) / (math.factorial(r) * (math.factorial(n-r)))

for n in range(1, 101):
    for r in range(1, n+1):
        choices = choose(n, r)
        if choices > 1000000:
            solutions.append((n, r, choices))

for solution in solutions:
    print(solution)
print(len(solutions))