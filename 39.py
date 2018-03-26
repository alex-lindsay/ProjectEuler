import math
solutions = []

# for p in range(1, 101):
for p in range(1, 1001):
    for a in range(1, int(p/2)):
        for b in range(a, p):
            c = p - a - b
            if math.sqrt(a**2 + b**2) == c:
                print(p, a, b, c)
                solutions.append((p, a, b, c))

result = {}
for (p, a, b, c) in solutions:
    if p not in result:
        result[p] = 0
    result[p] += 1

max_solutions = 0
max_result = 0
for (res, sol) in result.items():
    # print(sol, res)
    if sol > max_solutions:
        max_solutions = sol
        max_result = res

print("solutions", solutions)
print("result", result)
print("Result:", max_solutions, max_result)