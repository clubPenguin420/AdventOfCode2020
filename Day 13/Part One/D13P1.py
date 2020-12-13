def solve(lines):
    early = int(lines[0])
    ids = list(filter(("").__ne__, lines[1].replace("x", "").replace(",", " ").split(" ")))
    diffs = {}
    mini = early
    diff_index = 0
    for i in range(len(ids)):
        if abs((((early // int(ids[i])) + 1) * int(ids[i])) - early) < mini:
            diffs[i] = abs((((early // int(ids[i])) + 1) * int(ids[i])) - early)
            diff_index = i
    return min(diffs.values()) * int(ids[diff_index])


if __name__ == "__main__":
    inputs = []
    with open("Inputs.dat", "r") as f:
        for line in f.readlines():
            inputs.append(line)
    print(solve(inputs))
