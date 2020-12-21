import re
import sys

with open('Inputs.dat', 'r') as f:
    rules, strs = f.read().strip().split('\n\n')
    rules = rules.splitlines()
    rules = {int(a): r for a, r in [rule.split(': ') for rule in rules]}
    strs = strs.splitlines()

def resolve(rules, index, depth):
    if depth > 500:
        return ''
    rule = rules[index]
    if rule.startswith('"'):
        return rule.replace('"', '')
    else:
        ors = rule.split(' | ')
        r_ors = []
        for o in ors:
            cats = []
            for a in o.split(' '):
                r = resolve(rules, int(a), depth+1)
                # print(depth)
                cats.append(r)
            r_ors.append(''.join(cats))
        group = '|'.join(r_ors)
        return '(' + group + ')'

sys.setrecursionlimit(1013)

re_equiv = resolve(rules, 0, 0)

matches = [s for s in strs if re.fullmatch(re_equiv, s)]

print(len(matches))
#submit(a)