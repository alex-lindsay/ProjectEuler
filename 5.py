# divisors = range(1, 21)
# i = 22
# while True and i < 100000000:
#     if all([i % j == 0 for j in divisors]):
#         print(i)
#         break
#     if i % 100000 == 0:
#         print( 'testing %i' % i)

#     i += 1

# get highest exponent of each prime factor of all the items
factors = {}

for i in range(2,21):
    print("checking %i" % i)
    test = i
    factor = {}
    for j in range(2,i+1):
        # print("testing %i" % j)
        while (test % j == 0):
            # print("YES %i" % j)
            if (j in factor):
                factor[j] += 1
            else:
                factor[j] = 1
            test /= j

    print(factor)
    for (k,v) in factor.items():
        if k in factors:
            if v > factors[k]:
                factors[k] = v
        else:
            factors[k] = v

    print (factors)

result = 1
for (k,v) in factors.items():
    for i in range(1,v+1):
        result *= k

print(result)
for (k,v) in factors.items():
    for i in range(1, v+1):
        result /= k
        print(k,i,result)
