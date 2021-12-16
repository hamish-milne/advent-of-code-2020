def toint(s: str):
    i = 0
    for c in s.strip():
        i = (i << 1) | (1 if c == 'B' or c == 'R' else 0)
    return i
print(max(map(toint, open('day5.txt').readlines())))
