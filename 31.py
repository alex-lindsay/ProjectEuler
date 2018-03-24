coins = [1, 2, 5, 10, 20, 50, 100, 200]
partitions = {1: ["001"]}

def get_partitions(amt):
    if amt in partitions:
        return partitions[amt]

    result = []
    for coin in [coin for coin in coins if coin < amt]:
        remainder = amt - coin
        result = result + ["_".join(list(reversed(sorted((("00" + str(coin))[-3:] + \
            "_" + partition).split('_'))))) for partition in get_partitions(remainder)]

    if amt in coins:
        result = [("00" + str(amt))[-3:]] + result

    result = list(reversed(sorted(list(set(result)))))
    partitions[amt] = result
    print("get_partitions", amt, len(result))
    return result

for n in range(200, 201):
    # print(">>>", n, get_partitions(n))
    print(">>>", n, len(get_partitions(n)))

# print(partitions)
