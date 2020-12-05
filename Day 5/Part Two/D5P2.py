def solve(lines):
    big_id = 0
    seats = []
    for i in range(len(lines)):
        row_number = 0
        column_number = 0
        current_max = 127
        current_min = 0
        line = lines[i]
        rows = line[0:7]
        columns = line[7:]
        for j in rows:
            if(j == "F"):
                current_max = current_max - (((current_max - current_min) + 1) / 2)
            elif(j == "B"):
                current_min = current_min + (((current_max - current_min) + 1) / 2)
        row_number = current_max
        current_max = 7
        current_min = 0
        for k in columns:
            if(k == "L"):
                current_max = current_max - (((current_max - current_min) + 1) / 2)
            elif(k == "R"):
                current_min = current_min + (((current_max - current_min) + 1) / 2)
        column_number = current_max
        seats.append(row_number * 8 + column_number)
    
    return min(seat+1 for seat in seats if seat+1 not in seats and seat+2 in seats)


if __name__ == "__main__":
    inputs = []
    with open("Inputs.dat", "r") as f:
        for line in f.readlines():
            inputs.append(line)
    print(solve(inputs))
