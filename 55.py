solutions = []

last_number = 10000
max_iterations = 50

def is_palindrome(num):
    return str(num) == "".join(reversed(list(str(num))))

def flipped(num):
    return int("".join(reversed(list(str(num)))))

for n in range(1, last_number):
    i = 0
    test = n + flipped(n)
    while i<50 and not(is_palindrome(test)):
        test = test + flipped(test)
        i += 1
    
    if i==50:
        solutions.append(n)
        print(solutions)

print(len(solutions))