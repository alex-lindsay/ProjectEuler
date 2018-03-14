sum_of_squares = sum([x**2 for x in range(1,101)])
sum_squared = sum([x for x in range(1,101)]) ** 2

diff = abs(sum_squared - sum_of_squares)
print(diff)