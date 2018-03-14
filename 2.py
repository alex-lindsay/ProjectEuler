i = [0, 1]
n = sum(i)
total = 0
while n < 4000000:
    print n
    if n % 2 == 0:
        total += n
    i.append(n)
    del(i[0])
    n = sum(i)
print
print total
