def fibanoccilistreturn(n,m):
    f = list()
    f.append(0)
    f.append(1)
    for i in range(2,n+1):
        f.append((f[i-1]+f[i-2])%m)
        if (f[i]==1 and f[i-1]==0):
            return f[:len(f)-2]
    return f
def fibperiod(n,m):
    f = fibanoccilistreturn(m*m,m)
    l = len(f)
    print(l)
    return f[n%l]

n,m = map(int,input().split())
print(fibperiod(n,m))
