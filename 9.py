keepGoing = True
for a in range(1, 1000):
    if not keepGoing:
        break
    for b in range (1, a):
        if ((a%10==0) and (b%10==0)):
            print("Checking", a, b)
        c = 1000 - a - b
        if ((a**2)+(b**2)) == (c**2):
            print (a, b, c, a*b*c)
            keepGoing = False