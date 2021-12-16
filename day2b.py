valid = 0
for line in open('day2.txt').readlines():
    [policy, letter, pw] = line.split(' ')
    positions = [int(x) for x in policy.split('-')]
    pcount = sum(1 if pw[pos-1] == letter[0] else 0 for pos in positions)
    if pcount == 1:
        valid += 1
print(valid)
