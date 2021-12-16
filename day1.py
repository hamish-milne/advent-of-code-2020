from itertools import combinations
input = [int(x) for x in open('day1.txt').readlines()]
for c in combinations(input, 2):
    if c[0] + c[1] == 2020:
        print(c[0] * c[1])
        break
