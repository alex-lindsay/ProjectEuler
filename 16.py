data = [2]

index = 1

for index in range(2,1001):
    data = list(map(lambda i: i*2, data))

    for i in range(0,len(data)):
        if data[i] > 1000000000:
            if i == len(data)-1:
                data.append(0)
            data[i+1] += 1
            data[i] -= 1000000000

    print(">>>", index, data)

data.reverse()
data = "".join(list(map(lambda i: str(i), data)))
print(data)
print(sum(map(lambda x: int(x), list(data))))