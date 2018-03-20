with open("p022_names.txt") as sourceFile:
    source = sourceFile.read()
    sourceFile.close()

source = source.replace('"','').split(",")

print()
print(source[:10])
source.sort()
print(source[:10])

scores = [(index + 1) * sum([ord(letter)-64 for letter in list(name)]) for index, name in enumerate(source)]

print(scores[:10])

result = sum(scores)
print(result)