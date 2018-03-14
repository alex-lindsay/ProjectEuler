result = []
for i in range(0,21):
    # there is only one path along the top and left edge
    result.append([1])
    result[0].append(1)

print(result)
for i in range(1,21):
    for j in range(1,21):
        result[i].append(result[i-1][j] + result[i][j-1])

for i in range(0,21):
    print(result[i])

print(result[20][20])
