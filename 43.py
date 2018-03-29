def has_unique_digits(s):
    return len(s) == len(set(list(s)))

factors = [2, 3, 5, 7, 11, 13, 17]

prospects = [str(i) for i in range(0,9)]
print(0, prospects)

prospects = [prospect for prospect in \
    [a+("000"+str(b))[-3:] for a in prospects for b in range(0, 1000, 2)] \
    if has_unique_digits(prospect)]

print(2, len(prospects), prospects)

for factor in factors[1:]:
    prospects = [prospect for prospect in \
        [a+str(b)[-1] for a in prospects for b in range(0, 1000, factor) if (str(b).zfill(3)[:2] == a[-2:])] \
        if has_unique_digits(prospect)]
    print(factor, len(prospects), prospects[:10])
    
print("Result:", sum([int(prospect) for prospect in prospects]))
    