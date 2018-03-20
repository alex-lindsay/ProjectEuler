input = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

data = list(map(lambda s: s.split(" "), input.split("\n")))

def dump_data():
    for row in data:
        print(" ".join(row))
    print()

# data = data[0:5]
# print(data)
# print()

def search_tree(tree, row, col, curSum, curPath, maxSum, maxPath):
    if row >= len(tree):
        return (maxSum, maxPath)
    if col >= len(tree[row]):
        return (maxSum, maxPath)
    if tree[row][col] == "--":
        return (maxSum, maxPath)

    curPath.append((row, col))
    curSum += int(tree[row][col])
    if len(curPath) == len(tree):
        if curSum > maxSum:
            maxSum = curSum
            maxPath = curPath.copy()
        print(row, col, int(tree[row][col]), curSum, curPath)
        print(maxSum, maxPath)
        print()
    
    #first try going down
    (maxSum, maxPath) = search_tree(tree, row+1, col, curSum, curPath, maxSum, maxPath)

    #then try going diagonally
    (maxSum, maxPath) = search_tree(tree, row+1, col+1, curSum, curPath, maxSum, maxPath)
    curPath.pop()

    return (maxSum, maxPath)

# DOES NOT SOLVE OPTIMALLY
# for (rownum, row) in enumerate(data):
#     for (index, cell) in enumerate(row):
#         # remove elements that have better alternatives on either side
#         if (index > 0) and (index < len(row)-1):
#             if (cell < row[index-1]) and (cell < row[index+1]):
#                 # print(index, row[index-1], cell, row[index+1])
#                 row[index] = "--"

print()
dump_data()

(maxSum, maxPath) = search_tree(data, 0, 0, 0, [], 0, [])
print(maxSum, maxPath)