import math

def properDivisorsOf(aNumber):
    # print("properDivisorsOf(", aNumber,")")
    result = [1]
    for divisor in range(2, int(math.sqrt(aNumber)+1)):
        if aNumber % divisor == 0:
            result.append(divisor)
            if aNumber / divisor != divisor:
                result.append(int(aNumber / divisor))

    # print("result: ", result)
    return result

def isAbundant(aNumber):
    return sum(properDivisorsOf(aNumber)) > aNumber

abundantNumbers = list(filter(isAbundant, range(1, 28124)))
print(abundantNumbers[:10])

abundantSums = [a+b for a in abundantNumbers for b in abundantNumbers]
print(abundantSums[:10])
abundantSums = list(set([n for n in abundantSums if n < 28124]))
print(abundantSums[:10])
print(abundantSums[-10:])

notAbundantSums = [n for n in range(0, 28124) if n not in abundantSums]
print(notAbundantSums[:10])

print(sum(notAbundantSums))