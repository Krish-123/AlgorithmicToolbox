def selectionsort(l):
    for i in range(0,len(l)):
        minindex = i
        min = l[i]
        for j in range(i+1,len(l)):
            if l[j]<min:
                minindex = j
                min = l[j]
        #swap
        temp = l[i]
        l[i] = l[minindex]
        l[minindex] = temp
    return l

def merge(a,b,l):
    if len(a)==0:
        return l+b
    if len(b)==0:
        return l+a
    if a[0]<b[0]:
        l.append(a[0])
        return merge(a[1:],b,l)
    else:
        l.append(b[0])
        return merge(a,b[1:],l)
    return l

def mergesort(l):
    if len(l) == 1:
        return l
    else:
        mid = len(l)/2
        a = mergesort(l[:mid])
        b = mergesort(l[mid:])
        # print(a+b)
        l = list()
        return(merge(a,b,l))

print(selectionsort([12,13,121,12,1,1,2,14,32,34,23,17,63]))
print(mergesort([12,13,121,12,1,1,2,14,32,34,23,17,63]))
