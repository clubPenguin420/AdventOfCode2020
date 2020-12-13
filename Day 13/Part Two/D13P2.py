def solve(lines):
    bus,a=[],[]
    for i,d in enumerate(lines[0].split(',')):
        if d=='x':
            continue
        bus.append(int(d))    
        a.append(-i)

    def crt(a,b):
        if a-b==1:
            return 1,-1
        q,r=a//b,a%b
        m,n=crt(b,r)
        return n,m-n*q

    prod=1
    for b in bus:
        prod*=b

    ans=0
    for i,b in enumerate(bus):
        m,n=crt(prod//b,b)
        ans+=a[i]%b*m*prod//b

    return ans%prod


if __name__ == "__main__":
    inputs = open("Inputs.dat", "r").read().split("/n")
    print(solve(inputs))
