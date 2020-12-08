def solve(lines):
    acc = 0
    pos = 0
    pos_num_so_far = []

    while not pos in pos_num_so_far:
        line = lines[pos]
        inst = line[0:3]
        arg = line[4:]

        pos_num_so_far.append(pos)

        if inst == "acc":
            acc += int(arg)
            pos += 1
        elif inst == "jmp":
            pos += int(arg)
        else:
            pos += 1

    return acc


if __name__ == "__main__":
    inputs = []
    with open("Inputs.dat", "r") as f:
        for line in f.readlines():
            inputs.append(line)
    print(solve(inputs))
