from math import cos, radians, sin
(we, wn, pe, pn) = (10, 1, 0, 0)
for line in open('day12.txt').readlines():
    a = line[0]
    b = int(line[1:])
    if a == 'N':
        wn += b
    elif a == 'S':
        wn -= b
    elif a == 'E':
        we += b
    elif a == 'W':
        we -= b
    elif a == 'L' or a == 'R':
        if a == 'R':
            b = -b
        (cosb, sinb) = (round(cos(radians(b))), round(sin(radians(b))))
        (we, wn) = (
            we*cosb - wn*sinb,
            we*sinb + wn*cosb
        )
    elif a == 'F':
        pe += we * b
        pn += wn * b
print(abs(pe) + abs(pn))
