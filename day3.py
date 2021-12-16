trees = [ [c == '#' for c in line.strip()] for line in open('day3.txt').readlines() ]
width = len(trees[0])
print(sum(1 if trees[y][(y*3)%width] else 0 for y in range(len(trees))))
