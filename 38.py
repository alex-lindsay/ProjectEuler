solutions = []

#since we need more than one product we need no more than four digits in the multiplier

for a in range(1,10000):
    s = ""
    c = ""
    for b in range(1,10):
        s += str(a * b)
        c += str(b)
        if len(s) >= 9:
            break
    if len(s) != 9:
        continue
    if (len(set(list(s))) == 9) and ("0" not in list(s)):
        print(a, c, s)