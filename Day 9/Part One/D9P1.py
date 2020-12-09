import re
import math 

def solve(lines):
    n = len(lines)

    for x in range(25, n):
        good = False

        for y in range(x-25, x-1):
            if good:
                break

            for z in range(y+1, x):
                if lines[y] + lines[z] == lines[x]:
                    good = True
                    break
                
        if not good:
            return lines[x]



if __name__ == "__main__":
    inputs = []
    with open("Inputs.dat", "r") as f:
        for line in f.readlines():
            inputs.append(int(line))
    print(solve(inputs))
