cache = {1: []}

def collatz(n):
    if n not in cache:
        nextN = int((n%2 == 0) and (n/2) or ((3*n) + 1))
        print(n, nextN)
        cache[n] = [nextN] + collatz(nextN)

    return cache[n]

maxLen = 0
maxI = 0
# for i in range(1, 11):
for i in range(1, 1000001):
    c = collatz(i)
    if (len(c) > maxLen):
        maxLen = len(c)
        maxI = i
        print(i, len(c), maxI, maxLen)
    
    if i%1000 == 0:
        print(">>>", i, len(c), maxI, maxLen)

print(len(c), maxI, maxLen)
