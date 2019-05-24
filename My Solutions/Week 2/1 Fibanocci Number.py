def fibrec(n):
    print(n)
    if n<=1:
        return n
    return fibrec(n-1)+fibrec(n-2)
def fibanocci(n):
    f = list()
    f.append(0)
    f.append(1)
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    return f
def fibstore2num(n):
    twostepsago = 0
    onestepago = 1
    for i in range(2,n+1):
        value = twostepsago+onestepago
        twostepsago = onestepago
        onestepago = value
    return value

n = int(input())
# c = int(input())
# print([i%c for i in fibanocci(n)])
print(fibstore2num(n))
