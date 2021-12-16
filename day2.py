valid = 0
for line in open('day2.txt').readlines():
    [policy, letter, pw] = line.split(' ')
    [cmin, cmax] = [int(x) for x in policy.split('-')]
    if pw.count(letter[0]) in range(cmin, cmax+1):
        valid += 1
print(valid)
