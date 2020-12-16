def solve():
	instr = [int(num) for num in "6,4,12,1,20,0,16".split(",")]

	speak = {}
	counter = 1
	for i in instr[:-1]:
		speak[str(i)] = counter
		counter += 1
	last = str(instr[-1])
	while counter < 2020:
		if last not in speak.keys():
			speak[last] = counter
			last = "0"
			counter += 1
		else:
			diff = counter - speak[last]
			speak[last] = counter
			last = str(diff)
			counter += 1

	return last
	
print(solve())