from math import cos, sin, radians
(h, e, n) = (0, 0, 0)
for line in open('day12.txt').readlines():
    a = line[0]
    b = int(line[1:])
    if a == 'N':
        n += b
    elif a == 'S':
        n -= b
    elif a == 'E':
        e += b
    elif a == 'W':
        e -= b
    elif a == 'L':
        h += b
    elif a == 'R':
        h -= b
    elif a == 'F':
        e += int(cos(radians(h)) * b)
        n += int(sin(radians(h)) * b)
print(abs(e) + abs(n))
