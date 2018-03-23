import math

def is_prime(n):
    if n <= 1:
        return False
    for factor in range(2,int(math.sqrt(n)+1)):
        if n % factor == 0:
            return False

    # print(n, "is prime")
    return True

max_n = 0
max_n_a = None
max_n_b = None

for a in range(-999, 1000):
    for b in range (-1000, 1001):
# for a in range(1, 2):
#     for b in range (41, 42):
        n = 0
        test = (n**2) + (a * n) + b
        while is_prime(test):
            n += 1
            print (a, b, n, test)
            test = (n**2) + (a * n) + b
        if n > max_n:
            max_n = n
            max_n_a = a
            max_n_b = b
            print(">>", max_n_a, max_n_b, max_n, (max_n_a * max_n_b))

print("Result: ", max_n_a, max_n_b, max_n, (max_n_a * max_n_b))
