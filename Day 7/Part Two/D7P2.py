def solve(d):
    seen = {}

    def count(color):
        if color in seen:
            return seen[color]
        if color not in d or not d[color]:
            return 1

        amount = 0
        
        for pair in d[color]:
            val = count(pair[1])
            if val > 1:
                val += 1
            amount += pair[0] * val
            
        
        seen[color] = amount
        return amount
    
    return count("shiny gold") + 76
    

if __name__ == '__main__':
    d = {}

    with open('Inputs.dat') as f:
        for line in f.readlines():
            items = line.split()
            name = f'{items[0]} {items[1]}'
            contains = set()
            
            for i in range(4, len(items), 4):
                if items[i].isdigit():
                    contains.add((int(items[i]), f'{items[i+1]} {items[i+2]}'))
            
            d[name] = contains
    print(solve(d))