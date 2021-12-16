from typing import Set

code = [(l[0], int(l[1])) for l in (line.split(' ') for line in open('day8.txt').readlines()) ]
def terminates():
    acc = 0
    pc = 0
    executed: Set[int] = set()
    while pc not in executed:
        if pc >= len(code):
            print(acc)
            return True
        executed.add(pc)
        (instr, op) = code[pc]
        if instr == 'acc':
            acc += op
            pc += 1
        elif instr == 'jmp':
            pc += op
        elif instr == 'nop':
            pc += 1
    return False
for i in range(len(code)):
    (instr, op) = code[i]
    if instr == 'jmp':
        code[i] = ('nop', op)
    elif instr == 'nop':
        code[i] = ('jmp', op)
    else:
        continue
    if terminates():
        break
    code[i] = (instr, op)
