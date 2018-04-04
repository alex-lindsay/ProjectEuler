def digit_set(num):
    return sorted(list(str(num)))

num = 1
while True:
    if (num % 1000) == 0:
        print("Testing", num)
    family_digits = [digit_set(num * factor) for factor in range(1,7)]
    num_digits = family_digits[0]
    # print(family_digits)
    if all([digits == num_digits for digits in family_digits]):
        print("Result:", num, family_digits)
        break
    
    num += 1
    if num == 100000000:
        break