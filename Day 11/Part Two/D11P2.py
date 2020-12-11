def solve(lines):
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
                dirs = [[-1, -1], [-1, 0], [-1, 1], [1, -1], [1, 0], [0, -1], [1, 1], [0, 1]]

                for dy, dx in dirs:
                    diry = dy
                    dirx = dx

                    while 0 <= y+diry < height and 0 <= x+dirx < width:
                        if lines[y+diry][x+dirx] in ["L", "#"]:
                            if lines[y+diry][x+dirx] == '#':
                                occupied += 1
                            break

                        diry += dy
                        dirx += dx

                if c == 'L' and occupied == 0:
                    newlines[y][x] = '#'
                    changed = True
                if c == '#' and occupied >= 5:
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