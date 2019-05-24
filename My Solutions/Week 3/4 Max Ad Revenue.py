def merge(a,b,s):
    if len(a)==0:
        return s+b
    if len(b)==0:
        return s+a
    if a[0]<=b[0]:
        s.append(a[0])
        return merge(a[1:],b,s)
    else:
        s.append(b[0])
        return merge(a,b[1:],s)

def mergesort(a):
    if len(a) <= 1:
        return a
    mid = len(a)/2
    l = mergesort(a[:mid])
    m = mergesort(a[mid:])

    s = list()
    return merge(l,m,s)

def MaxRevenue(a,b):
    a = mergesort(a)
    b = mergesort(b)
    sum = 0
    for i in range(len(a)):
        sum += a[i]*b[i]
    return sum

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

print(MaxRevenue(a,b))
