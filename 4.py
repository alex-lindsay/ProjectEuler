import sys
result = 0
for i in xrange(999, 100, -1):
    for j in xrange(i, 100, -1):
        p = str(i*j)
        if p == p[::-1]:
            if int(p) > result:
                result = int(p)
                print i, j, p

print p
