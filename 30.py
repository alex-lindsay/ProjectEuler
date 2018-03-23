def quint_sum(n):
    result = 0
    while n>0:
        result += (n % 10)**5
        n = int(n/10)
    return result

total = 0
for n in range(2, 1000000):
    if n % 100000 == 0:
        print(n)
    q = quint_sum(n)
    if q == n:
        print(n, q)
        total += n

print("Result:", total)