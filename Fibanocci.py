def fibanocci(n):
    if n<=1:
        return n
    else:
        return(fibanocci(n-1)+fibanocci(n-2))

def fibanoccifast(n):
    F = list()
    F.append(0)
    F.append(1)
    for i in range(2,n+1):
        F.append(F[i-1]+F[i-2])
    return F[n]
n = int(input())
print(fibanoccifast(n))
