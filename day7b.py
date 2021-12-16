from typing import Dict, List, Tuple

rules: Dict[str, List[Tuple[int, str]]] = {}
for line in open('day7.txt').readlines():
    [src, rulestr] = line.split(' bags contain ')
    if rulestr.startswith('no other'):
        rules[src] = []
    else:
        rules[src] = [(int(r[:r.index(' ')]), r[r.index(' ')+1:r.rindex(' ')]) for r in rulestr.split(', ')]
def countbags(src: str)->int:
    return sum(r[0] + r[0]*countbags(r[1]) for r in rules[src])
print(countbags('shiny gold'))
