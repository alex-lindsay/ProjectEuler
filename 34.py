import math

solutions = []

for n in range(3,10000000):
    i = sum([math.factorial(int(d)) for d in list(str(n))])
    if i == n:
        print(n)
        solutions.append(n)

print(solutions)
print("Result:", sum(solutions))