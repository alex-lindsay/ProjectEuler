# size = 5
size = 1001

total = 1
increment = 2
corner = 1
while (corner <= size**2):
    for i in range(0,4):
        corner = corner + increment
        if (corner <= size**2):
            total += corner
            print(increment, corner, total)
    
    increment += 2

print(total)