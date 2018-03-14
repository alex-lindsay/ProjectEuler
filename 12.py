from math import sqrt

def triangle(n):
    return int((n * (n-1))/2)

def factors(n):
    result = [1,n]
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            result.append(i)
            result.append(i / n)
    return result

x=1
while (True):
    tri = triangle(x)
    triFact = factors(triangle(x))
    if (x % 100 == 0):
        print(x, tri, len(triFact))
    if len(triFact) > 500:
        break
    x += 1

print(x, tri, len(triFact))