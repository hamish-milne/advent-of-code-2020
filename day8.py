from typing import Set

code = [(l[0], int(l[1])) for l in (line.split(' ') for line in open('day8.txt').readlines()) ]
acc = 0
pc = 0
executed: Set[int] = set()
while pc not in executed:
    executed.add(pc)
    (instr, op) = code[pc]
    if instr == 'acc':
        acc += op
        pc += 1
    elif instr == 'jmp':
        pc += op
    elif instr == 'nop':
        pc += 1
print(acc)
