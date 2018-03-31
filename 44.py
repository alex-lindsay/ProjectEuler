import time

pentagonals = [0]

def pentagonal(num):
    if num >= len(pentagonals):
        start = len(pentagonals)
        for i in range(start, num+1):
            # print(num, start, i)
            pentagonals.append(int((i * ((3 * i) - 1)) / 2))
            # print(">", pentagonals)

    # print(pentagonals, num)
    return pentagonals[num]

def add_pentagonals(stop_after):
    while pentagonals[-1] < stop_after:
        pentagonal(len(pentagonals))
    # print(pentagonals)

a = 2
keep_going = True
solutions = []
while keep_going:
    if a % 1000 == 0:
        print("Checking a:", a)
        print(solutions)
        print()
        time.sleep(0.5)
    p_a = pentagonal(a)
    for b in range(1, a):
        if b % 1000 == 0:
            print("Checking b:", b)
        p_b = pentagonal(b)
        if (p_a - p_b) in pentagonals:
            # print(a, b, p_a, p_b, p_a-p_b, "diff is pentagonal")
            # time.sleep(2)
            add_pentagonals(p_a + p_b)
            if (p_a + p_b) in pentagonals:
                print(a, b, p_a, p_b, p_a+p_b, "sum is pentagonal")
                solutions.append((p_a, p_b, p_a-p_b))
                print(solutions)
                time.sleep(5)
                keep_going = (len(solutions) < 5) and (a < 10)

    a += 1