def solve(lines):
    y = 0
    x = 0
    wx = -10 
    wy = 1

    for line in lines:
        act = line[0:1]
        value = int(line[1:])

        if act == "F":
          x += value * wx
          y += value * wy
        elif act == "E":
          wx -= value
        elif act == "W":
          wx += value
        elif act == "S":
          wy -= value
        elif act == "N":
          wy += value
        elif act == "L":
          for _ in range(value // 90):
            wx, wy = (wy, -wx)
        elif act == "R":
          for _ in range(value // 90):
            wx, wy = (-wy, wx)
    
    return abs(x) + abs(y)


if __name__ == "__main__":
    inputs = []
    with open("Inputs.dat", "r") as f:
        for line in f.readlines():
            inputs.append(line)
    print(solve(inputs))
