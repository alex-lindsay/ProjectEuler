def long_division(numerator, denominator, quotient_string):
    # print("long_division", numerator, denominator)
    while numerator < denominator:
        numerator *= 10
        quotient_string += "0"

    quotient_string += str(int(numerator / denominator))
    remainder = numerator % denominator
    print("long_division >> ", numerator, denominator, remainder, quotient_string)
    return (remainder, quotient_string)


max_repeater_length = 0
max_repeater_denominator = 1
for denominator in range(2, 1001):
    numerator = 1
    remainders = []
    remainder = -1
    quotient_string = ""
    while (remainder != 0):
        (remainder, quotient_string) = long_division(numerator, denominator, quotient_string)
        if remainder in remainders:
            break
        remainders.append(remainder)
        numerator = remainder * 10

    repeater_length = 0
    if remainder != 0:
        repeater_length = len(remainders) - remainders.index(remainder)
    if repeater_length > max_repeater_length:
        max_repeater_length = repeater_length
        max_repeater_denominator = denominator
        print("***", max_repeater_denominator, max_repeater_length)

    print(denominator, quotient_string, remainder, remainders, repeater_length)

print("Result:")
print("***", max_repeater_denominator, max_repeater_length)

