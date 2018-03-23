terms = {}

for a in range(2, 101):
    for b in range(2, 101):
        terms[a**b] = 1

print("Result:", len(terms.keys()))