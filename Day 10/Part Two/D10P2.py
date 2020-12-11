def solve(lines):
    lines.append(max(lines) + 3)
    x = len(lines)
    seen = {}

    def count(pos):
        if pos == x - 1:
            return 1

        if pos in seen:
            return seen[pos]

        combs = count(pos+1)

        if pos < x-2 and lines[pos+2] - 3 <= lines[pos]:
            combs += count(pos+2)
        if pos < x-3 and lines[pos+3] - 3 <= lines[pos]:
            combs += count(pos+3)

        seen[pos] = combs

        return combs

    return count(0)


if __name__ == "__main__":
    inputs = [0]
    with open("Inputs.dat", "r") as f:
        for line in f.readlines():
            inputs.append(int(line))
    print(solve(sorted(inputs)))
