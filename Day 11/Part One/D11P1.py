def solve(lines):
    def state_farms(y, x):
        state_farms = []

        if y > 0:
            state_farms.append([y-1, x])
            if x > 0:
                state_farms.append([y-1, x-1])
            if x < 93:
                state_farms.append([y-1,x+1])
        if y < 96:
            state_farms.append([y+1, x])
            if x > 0:
                state_farms.append([y+1, x-1])
            if x < 93:
                state_farms.append([y+1,x+1])
        if x > 0:
            state_farms.append([y, x-1])
        if x < 93:
            state_farms.append([y, x+1])

        return state_farms

    height = len(lines)
    width = len(lines[0])

    while True:
        changed = False
        newlines = [list(line) for line in lines]

        for y in range(height):
            for x in range(width):
                c = lines[y][x]

                if c == '.':
                    continue

                occupied = 0

                for dy, dx in state_farms(y, x):
                    if lines[dy][dx] == '#':
                        occupied += 1

                if c == 'L' and occupied == 0:
                    newlines[y][x] = '#'
                    changed = True
                if c == '#' and occupied >= 4:
                    newlines[y][x] = 'L'
                    changed = True

        if not changed:
            break

        lines = newlines
        
    return sum(sum(c == '#' for c in row) for row in lines)


if __name__ == '__main__':
    lines = []
    with open('Inputs.dat') as f:
        for line in f.readlines():
            lines.append(line.rstrip())

    print(solve(lines))