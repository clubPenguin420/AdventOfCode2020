def solve(lines):
    lines.append(max(lines) + 3)
    one_diff = 0
    three_diff = 0
    done = False
    current_num = 0
    pos = 0
    while pos < len(lines) - 1:
        next_num = lines[pos + 1]
        if next_num - current_num == 1:
            one_diff += 1
        elif next_num - current_num == 3:
            three_diff += 1
        pos += 1
        current_num = next_num

    # print(lines)
    return one_diff * three_diff


if __name__ == "__main__":
    inputs = [0]
    with open("Inputs.dat", "r") as f:
        for line in f.readlines():
            inputs.append(int(line))
    print(solve(sorted(inputs)))
