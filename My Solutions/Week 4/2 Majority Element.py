#Using this function in mergesort
def merge(a,b,out):
    if len(a)==0:
        out = out+b
        return out
    if len(b)==0:
        out = out+a
        return out
    if a[0]<b[0]:
        out.append(a[0])
        return merge(a[1:],b,out)
    else:
        out.append(b[0])
        return merge(a,b[1:],out)
#Using this function in majorityelement
def mergesort(l):
    if len(l)==1:
        return l
    m = len(l)/2
    a = mergesort(l[:m])
    b = mergesort(l[m:])
    out = []
    return merge(a,b,out)
def majorityelement(l):
    l = mergesort(l)
    c = l[0]
    count = 1
    for i in range(len(l)):
        if l[i]==c:
            count+=1
        else:
            if count>len(l)/2:
                return 1
            c = l[i]
            count = 1
    return 0

# Using this function in majorityelement2
def checkelement(l,c):
    count = 0
    for i in l:
        if i==c:
            count+=1
    if count>len(l)/2:
        return 1
    else:
        return 0
def majorityelement2(l):
    if len(l)==1:
        return l[0]
    m = len(l)/2
    a = majorityelement2(l[:m])
    b = majorityelement2(l[m:])
    if a==-1 and b==-1:
        return -1
    maj = -1
    if checkelement(l,a):
        maj = a
    elif checkelement(l,b):
        maj = b
    return maj

l = [2,2,2,3,5,3,4,5]
if majorityelement2(l)==-1:
    print(0)
else:
    print(1)
