def moneychange(n,d):
    # Each and every sub problem will be calculated and stored in a list
    l = [0]
    for i in range(1,n+1):
        minimum = None
        for j in range(len(d)):
            if d[j]>i:
                continue
            try:
                if l[i-d[j]] == -1:
                    continue
                if minimum is None or l[i-d[j]]+1 < minimum:
                    minimum = l[i-d[j]]+1
            except:
                print(i,j)
        if minimum is None:
            l.append(-1)
        else:
            l.append(minimum)
    return l[n]

def moneychangerecursive(n,d,T):
    # Ideal in cases where you are not using all the sub problems
    if n == 0:
        T[n] = 0
    elif n<min(d):
        # print(n)
        T[n] = -1
    if n not in T:
        minimum = None
        for i in range(len(d)):
            if d[i]>n:
                continue
            # print(d[i])
            c,T = moneychangerecursive(n-d[i],d,T)
            if c == -1:
                continue
            else:
                c += 1
            # print(c)
            if minimum is None or c<minimum:
                minimum = c
        if minimum is None:
            T[n] = -1
        else:
            T[n] = minimum
        # print(minimum)
    return T[n],T

T = {}
print(moneychange(31,[1,6,20,25]))
c,T = moneychangerecursive(34,[3,6,20,25],T)
print(c,T)
