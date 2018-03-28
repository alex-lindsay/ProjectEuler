champernowne = ""
a = 1
while len(champernowne) < 1000001:
    champernowne += str(a)
    a += 1

print(champernowne)

# result = int(champernowne[0])
result = 1
for i in range(0,7):
    print(10 ** i - 1, champernowne[10 ** i - 1])
    result *= int(champernowne[10 ** i - 1])

print("Result:", result)