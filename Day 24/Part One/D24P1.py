def black_count(map):
    return list(map.values()).count(True)

paths = []
with open("Inputs.dat") as f:
    for line in f:
        dirs = []
        l = iter(line.strip())
        dir = next(l)
        for ch in l:
            if dir in ("e", "w") or len(dir) == 2:
                dirs.append(dir)
                dir = ch
            else:
                dir += ch
        dirs.append(dir)
        paths.append(dirs)

map = {}
for path in paths:
    coords = [0, 0]
    for dir in path:
        if dir == "e":
            coords[0] += 1
        elif dir == "w":
            coords[0] -= 1
        elif dir == "nw":
            coords[1] -= 1
        elif dir == "se":
            coords[1] += 1
        elif dir == "sw":
            coords[0] -= 1
            coords[1] += 1
        elif dir == "ne":
            coords[0] += 1
            coords[1] -= 1
    coords = tuple(coords)
    map[coords] = not map.get(coords, False)

print(black_count(map))