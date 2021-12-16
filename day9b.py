from typing import List
from itertools import combinations

code = [int(s) for s in open('day9.txt').readlines()]
buf: List[int] = []
found = 0
for n in code:
    if len(buf) < 25:
        buf.append(n)
        continue
    if not any(c[0]+c[1] == n for c in combinations(buf, 2)):
        found = n
        break
    buf.append(n)
    buf.pop(0)
for s in range(len(code)-1):
    for e in range(s, len(code)-1):
        sl = code[s:e+2]
        if sum(sl) == found:
            print(min(sl) + max(sl))
            exit()
