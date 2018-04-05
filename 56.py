def digit_sum(num):
    return sum([int(x) for x in list(str(num))])

max_digit_sum = 0

for a in range(1, 100):
    for b in range(1, 100):
        s = digit_sum(a**b)
        if s > max_digit_sum:
            print(a, b, s)
            max_digit_sum = s

print(max_digit_sum)