import itertools

digits = [str(x) for x in range(10)]
print(digits)

permutationIndex = 0
result = ""

for digitPermutation in itertools.permutations(digits):
    permutationIndex += 1
    if permutationIndex % 100000 == 0:
        print(permutationIndex, digitPermutation)

    if permutationIndex == 1000000:
        result = "".join(digitPermutation)
        break

print(result)