def solve(lines):
    big_id = 0
    for i in range(len(lines)):
        row_number = 0
        column_number = 0
        current_max = 127
        current_min = 0
        line = lines[i]
        rows = line[0:7]
        columns = line[7:]
        for i in rows:
            if(i == "F"):
                current_max = current_max - (((current_max - current_min) + 1) / 2)
            elif(i == "B"):
                current_min = current_min + (((current_max - current_min) + 1) / 2)
        row_number = current_max
        current_max = 7
        current_min = 0
        for i in columns:
            if(i == "L"):
                current_max = current_max - (((current_max - current_min) + 1) / 2)
            elif(i == "R"):
                current_min = current_min + (((current_max - current_min) + 1) / 2)
        column_number = current_max
        if(big_id >= row_number * 8 + column_number):
            continue
        else:
            big_id = row_number * 8 + column_number

    return big_id

if __name__ == "__main__":
    inputs = []
    with open("Inputs.dat", "r") as f:
        for line in f.readlines():
            inputs.append(line)
    print(solve(inputs))
