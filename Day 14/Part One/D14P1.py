with open('Inputs.dat', 'r') as f:
    prog = []
    for line in f.read().strip().splitlines():
        if line.startswith('mask ='):
            prog.append(('mask', line.split(' = ')[1]))
        else:
            a, value = line.split(' = ')
            addr = a.split('[')[1].split(']')[0]
            addr = int(addr)
            value = int(value)
            prog.append((addr, value))

 
mem = {}
mask = None


def write(addr, val):
    val = bin(val)[2:]
    val = val.zfill(len(mask))
    new_val = [m if m != 'X' else v for m, v in zip(mask, val)]
    new_val = ''.join(new_val)
    mem[addr] = int(new_val, 2)


for addr, value in prog:
    if addr == 'mask':
        mask = value
    else:
        write(addr, value)


s = 0

for addr, value in mem.items():
    s += value


print(s)