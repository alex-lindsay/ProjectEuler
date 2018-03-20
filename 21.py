import math

def properDivisorsOf(aNumber):
    print("properDivisorsOf(", aNumber,")")
    result = [1]
    for divisor in range(2, int(math.sqrt(aNumber)+1)):
        if aNumber % divisor == 0:
            result.append(divisor)
            if aNumber / divisor != divisor:
                result.append(int(aNumber / divisor))

    print("result: ", result)
    return result


divisorSums = [0]
amicableNumbers = []
testNumber = 1
while testNumber <= 10000:
# while testNumber <= 100:
    divisorSums.append(sum(properDivisorsOf(testNumber)))
    testNumber += 1

print(divisorSums)
for x in range(0, len(divisorSums)):
    # print(x, divisorSums[x])
    if (divisorSums[x] < len(divisorSums)) and \
        (divisorSums[x] > x) and \
        (divisorSums[divisorSums[x]] == x) :
        print(x, divisorSums[x])
        amicableNumbers.append(x)
        amicableNumbers.append(divisorSums[x])

print(amicableNumbers)

print(sum(amicableNumbers))
        