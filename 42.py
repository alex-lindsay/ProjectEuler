import math
words = []
with open("p042_words.txt") as infile:
    words = infile.read().replace('"',"").split(",")

# print(words)

scores = [sum([ord(letter)-ord('A')+1 for letter in list(word)]) for word in words]
max_score = max(scores)

print(scores, max_score)

triangles = [n for n in [sum(range(1,n+1)) for n in range(1, 100)] if n <= max_score]
print(triangles)

solutions = [(index, word, scores[index]) for (index, word) in enumerate(words) if scores[index] in triangles]

print(solutions)
print("Result:", len(solutions))