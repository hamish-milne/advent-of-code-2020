adp = [int(x) for x in open('day10.txt').readlines()]
adp.sort()
diffs = [0]*4
current = 0
for n in adp:
    diffs[n - current] += 1
    current = n
diffs[3] += 1
print(diffs[1] * diffs[3])
