solutions = []

def is_binary_palindrome(num):
    binary = '{0:b}'.format(num)
    print(num, binary)
    for i in range(0, int(len(binary)/2)):
        if binary[i] != binary[-(i+1)]:
            return False
    return True

for a in range(1, 10):
    if is_binary_palindrome(a):
        solutions.append(a)

# for a in range(1, 10):
for a in range(1, 1000):
    b = str(a)
    #test even length palindrome
    z = b[::-1]
    if is_binary_palindrome(int(b + z)):
        solutions.append(int(b + z))
    
    #test odd length palindromes
    if len(b) < 3:
        for m in range(0,10):
            if is_binary_palindrome(int(b + str(m) + z)):
                solutions.append(int(b + str(m) + z))


print(solutions)
print("Result:", sum(solutions))