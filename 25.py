fib = [1, 1, 1]

def fibonacci(n):
    if (n < len(fib)) and (fib[n] is not None):
        return fib[n]
    if n <= 2:
        return 1
    else:
        fib.append(fibonacci(n-1) + fibonacci(n-2))
        return fibonacci(n-1) + fibonacci(n-2)

n=1
while len(str(fibonacci(n))) < 1000:
    if n % 5 == 0:
        print(n, fib[n])
    n += 1

print("The index is", n, "and the number is", fibonacci(n))