def merge(a,b,out,inv):
    if len(a) == 0:
        return out+b,inv
    if len(b) == 0:
        return out+a,inv
    if a[0]<=b[0]:
        out.append(a[0])
        return merge(a[1:],b,out,inv)
    else:
        out.append(b[0])
        inv += len(a)
        return merge(a,b[1:],out,inv)
def mergesortwithinvcount(l):
    inv = 0
    if len(l) <= 1:
        return l,inv
    m = len(l)/2
    a,inv1 = mergesortwithinvcount(l[:m])
    b,inv2 = mergesortwithinvcount(l[m:])
    inv = inv1+inv2
    out = []
    out,inv = merge(a,b,out,inv)
    return out,inv
l = [2,3,9,2,9]
l,inv = mergesortwithinvcount(l)
print(inv)
