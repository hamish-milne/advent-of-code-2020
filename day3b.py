trees = [ [c == '#' for c in line.strip()] for line in open('day3.txt').readlines() ]
width = len(trees[0])
total = 1
for (r,d) in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    result = 0
    i = 0
    while i*d < len(trees):
        if trees[i*d][(i*r)%width]:
            result += 1
        i += 1
    total *= result
print(total)
