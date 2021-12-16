def toint(s: str):
    i = 0
    for c in s.strip():
        i = (i << 1) | (1 if c == 'B' or c == 'R' else 0)
    return i
seats = set(map(toint, open('day5.txt').readlines()))
seats.symmetric_difference_update(range(min(seats), max(seats)+1))
print(list(seats)[0])
