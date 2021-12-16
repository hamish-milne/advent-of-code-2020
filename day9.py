from typing import List
from itertools import combinations


buf: List[int] = []
for n in (int(s) for s in open('day9.txt').readlines()):
    if len(buf) < 25:
        buf.append(n)
        continue
    if not any(c[0]+c[1] == n for c in combinations(buf, 2)):
        print(n)
        break
    buf.append(n)
    buf.pop(0)
