def ang_to(ang):
    if ang == 90:
        return -1, 0
    elif ang == 180:
        return 0, -1
    elif ang == 270:
        return 1, 0
    elif ang == 0:
        return 0, 1

def solve(lines):
    y = 0
    x = 0
    ang = 90
    dirx, diry = ang_to(ang)

    for line in lines:
        act = line[0:1]
        value = int(line[1:])

        if act == "F":
            x += dirx * value
            y += diry * value
        elif act == "E":
            x -= value
        elif act == "W":
            x += value
        elif act == "S":
            y -= value
        elif act == "N":
            y += value
        elif act == "L":
            ang = (ang - value + 360) % 360
            dirx, diry = ang_to(ang)
        elif act == "R":
            ang = (ang + value + 360) % 360
            dirx, diry = ang_to(ang)
    
    return abs(x) + abs(y)


if __name__ == "__main__":
    inputs = []
    with open("Inputs.dat", "r") as f:
        for line in f.readlines():
            inputs.append(line)
    print(solve(inputs))
