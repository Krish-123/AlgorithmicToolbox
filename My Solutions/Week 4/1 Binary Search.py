def binarysearch(l,c,low,high):
    if low>high:
        return -1
    m = low+(high-low)/2
    if l[m]>c:
        return binarysearch(l,c,low,m-1)
    elif l[m]<c:
        return binarysearch(l,c,m+1,high)
    else:
        return m

l = [1,2,3,4,5,6,7,8,9]
print(binarysearch(l,6,0,len(l)))
3
