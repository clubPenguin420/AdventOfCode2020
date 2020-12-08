def solve(lines):
    jmps = [x for x in range(len(lines)) if lines[x][0] == 'jmp']
    nops = [x for x in range(len(lines)) if lines[x][0] == 'nop']

    changes = [[x, 'nop'] for x in jmps] + [[x, 'jmp'] for x in nops]
    for changepos, change in changes:
        newprog = list(list(row) for row in lines)
        newprog[changepos][0] = change

        pos_num_so_far = []
        acc = 0
        pos = 0

        while pos not in pos_num_so_far:
            if pos == len(lines):
                return acc

            inst, val = newprog[pos]
            pos_num_so_far.append(pos)

            if inst == 'acc':
                acc += val
                pos += 1
            elif inst == 'jmp':
                pos += val
            elif inst == 'nop':
                pos += 1

if __name__ == '__main__':
    lines = []

    with open('Inputs.dat') as f:
        for line in f.readlines():
            sp = line.split()
            lines.append([sp[0], int(sp[1])])

    print(solve(lines))