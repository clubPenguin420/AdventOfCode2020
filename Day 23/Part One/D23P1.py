inputs = '326519478'

cups = list(map(int,inputs))
for _ in range(100):
    pc = cups[1:4]
    dest = cups[0] - 1
    if dest == 0:
        dest = 9
    while dest in pc:
        dest -= 1
        if dest == 0:
            dest = 9
    new_cups = cups[:1] + cups[4:]
    n_idx = new_cups.index(dest)
    new_cups = new_cups[:n_idx+1] + pc + new_cups[n_idx+1:]
    cups = new_cups[1:] + new_cups[:1]

print("".join(map(str,cups[cups.index(1)+1:] + cups[:cups.index(1)])))