def binarysearch(l,low,high,c):
    if low>high:
        return low-1
    m = low+(high-low)/2
    if l[m]==c:
        return m
    elif l[m]<c:
        return binarysearch(l,m+1,high,c)
    else:
        return binarysearch(l,low,m-1,c)

def merge(a,b,I1,I2,out1,out2):
    if len(a) == 0:
        out1 = out1+b
        out2 = out2+I2
        return out1,out2
    if len(b) == 0:
        out1 = out1+a
        out2 = out2+I1
        return out1,out2
    if a[0]<=b[0]:
        out1.append(a[0])
        out2.append(I1[0])
        return merge(a[1:],b,I1[1:],I2,out1,out2)
    else:
        out1.append(b[0])
        out2.append(I2[0])
        return merge(a,b[1:],I1,I2[1:],out1,out2)
def mergesort(l,I):
    if len(l) <= 1:
        return l,I
    m = len(l)/2
    a,I1 = mergesort(l[:m],I[:m])
    b,I2 = mergesort(l[m:],I[m:])
    out1 = []
    out2 = []
    l,I = merge(a,b,I1,I2,out1,out2)
    return l,I
def lottery(r,s):
    x = [i for i,j in r]
    y = [j for i,j in r]
    I1 = [i for i in range(len(x))]
    I2 = [i for i in range(len(y))]
    sx,Ix = mergesort(x,I1)
    sy,Iy = mergesort(y,I2)

    out = []
    for i in range(len(s)):
        m1 = binarysearch(sx,0,len(sx)-1,s[i])
        m2 = binarysearch(sy,0,len(sy)-1,s[i])
        if sy[m2] == s[i]:
            m2 = m2
        else:
            m2 = m2+1
        print(m1,m2)
        out.append(len(set(I1[:m1+1]).intersection(set(I2[m2:]))))
    return out

l = [[0,5],[-3,2],[4,10]]
s = [1,6,0,5]

print(lottery(l,s))
