solutions = []

for a in range(10,100):
    for b in range(a+1,100):
        if (a % 10 == 0) and (b % 10 == 0):
            continue
        if (a % 11 == 0) and (b % 11 == 0):
            continue
        if (b % 10 != 0) and ((int(a/10) / (b % 10)) == a/b) and ((a%10) == int(b/10)):
            print(a,b)
            solutions.append((a,b))
        elif (((a % 10) / int(b/10)) == a/b) and ((b%10) == int(a/10)):
            print(a,b)
            solutions.append((a,b))

print(solutions)
result = 1
for (numerator, denominator) in solutions:
    result *= (numerator / denominator)

print(1/result)