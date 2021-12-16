adp = [int(x) for x in open('day10.txt').readlines()]
adp.sort()
adp.append(adp[-1] + 3)
diffs = 0
current = 0
result = 1
for n in adp:
    if n - current == 1:
        diffs += 1
    else:
        if diffs > 2:
            result *= 3*(1 << (diffs-3)) + 1
        elif diffs == 2:
            result *= 2
        diffs = 0
    current = n
print(result)
