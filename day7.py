from typing import Dict, List, Tuple

rules: Dict[str, List[Tuple[int, str]]] = {}
for line in open('day7.txt').readlines():
    [src, rulestr] = line.split(' bags contain ')
    if rulestr.startswith('no other'):
        rules[src] = []
    else:
        rules[src] = [(int(r[:r.index(' ')]), r[r.index(' ')+1:r.rindex(' ')]) for r in rulestr.split(', ')]
def cancontain(src: str, dst: str)->bool:
    return any(dst == r[1] or cancontain(r[1], dst) for r in rules[src])
print(sum(1 if cancontain(x, 'shiny gold') else 0 for x in rules))
