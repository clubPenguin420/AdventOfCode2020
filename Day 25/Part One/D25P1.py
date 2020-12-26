inputs = open("Inputs.dat", "r").read().strip().splitlines()
card = int(inputs[0])
door = int(inputs[1])

transform = lambda val, sub_num: (val * sub_num) % 20201227
def getLoopSize(target_num):
    val = 1
    loops = 0
    while val != target_num:
        val = transform(val, 7)
        loops += 1
    return loops

def loopPKey(sub_num, loops):
    val = 1
    for _ in range(loops):
        val = transform(val, sub_num)
    return val
import time
start = time.time()
print(loopPKey(card, getLoopSize(door)))