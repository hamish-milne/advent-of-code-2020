from functools import reduce
from typing import List, Set
sets: List[Set[str]] = [
    reduce(
        set.intersection, # type: ignore
        (set(line) for line in group.splitlines(keepends=False))
    )
    for group in open('day6.txt').read().split('\n\n')
]
print(sum(map(len, sets)))