def primitivecalculator(n,T):
    if n not in T:
        if n == 0:
            T[n] = 0
            return T[n],T

        a,b,c = [None]*3
        if n%2 == 0:
            a,T = primitivecalculator(n/2,T)
        if n%3 == 0:
            b,T = primitivecalculator(n/3,T)
        c,T = primitivecalculator(n-1,T)
        if a is None and b is None:
            minimum = c+1
        elif a is None:
            minimum = min(b,c)+1
        elif b is None:
            minimum = min(a,c)+1
        else:
            minimum = min(a,b,c)+1
        T[n] = minimum
    return T[n],T

def operationsoutput(l,n):
    s = [n]
    current = n
    while current != 1:
        current = l[current]
        s.append(current)
    return(s)

def primcaliterative(n):
    if n==0:
        return 0
    T = [0,0]
    l = [0,0]
    for i in range(2,n+1):
        a,b,c = [float('inf')]*3
        if i%2 == 0:
            a = T[i/2]
        if i%3 == 0:
            b = T[i/3]
        c = T[i-1]
        minimum = min(a,b,c)+1
        T.append(minimum)
        if minimum == a+1:
            l.append(i/2)
        elif minimum == b+1:
            l.append(i/3)
        else:
            l.append(i-1)

    return T[-1],operationsoutput(l,n)

n = int(input())
T = {}
# print(primitivecalculator(n,T)[0])
print(primcaliterative(n))
