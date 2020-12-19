with open('Inputs.dat', 'r') as f:
    homework = f.read().strip().splitlines()

precedence = {
    '+': 1, 
    '*': 1, 
    '(': 3,
}

def sy(prob):
    prob = prob.replace(' ', '')
    args = []
    ops = []
    for c in prob:
        if c.isnumeric():
            args.append(int(c))
        elif c == '(':
            ops.append(c)
        elif c == ')':
            while ops[-1] != '(':
                args.append(ops.pop())
            ops.pop()
        else:
            assert c in precedence
            while ops and precedence[ops[-1]] <= precedence[c]:
                args.append(ops.pop())
            ops.append(c)
    stack = args + ops[::-1]
    return stack

def evaluate(prob):
    stack = sy(prob)
    ev = []
    for c in stack:
        if isinstance(c, int):
            ev.append(c)
        else:
            if c == '+':
                b = ev.pop()
                a = ev.pop()
                c = a + b
                ev.append(c)
            elif c == '*':
                b = ev.pop()
                a = ev.pop()
                c = a * b
                ev.append(c)
            else:
                assert False, c
    assert len(ev) == 1
    return ev[0]

res = []

for prob in homework:
    a = evaluate(prob)
    res.append(a)

a = sum(res)

print(a)