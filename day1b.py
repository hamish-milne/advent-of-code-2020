from itertools import combinations
from functools import reduce
from operator import mul
input = [int(x) for x in open('day1.txt').readlines()]
for c in combinations(input, 3):
    if sum(c) == 2020:
        print(reduce(mul, c))
        break
