def binarysearch(l,low,high,key):
    if low>high:
        return low-1
    mid = low+(high-low)/2
    if key==l[mid]:
        return mid
    elif key<l[mid]:
        return binarysearch(l,low,mid-1,key)
    elif key>l[mid]:
        return binarysearch(l,mid+1,high,key)

def binarysearchiterative(l,low,high,key):
    while low<=high:
        mid = low+(high-low)/2
        if key==l[mid]:
            return mid
        elif key<l[mid]:
            high = mid-1
        elif key>l[mid]:
            low = mid+1
    if low>high:
        return low-1

print(binarysearch([1,3,5,9,15,17,21,34],0,7,10))
print(binarysearchiterative([1,3,5,9,15,17,21,34],0,7,22))
