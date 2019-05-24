# python 3
def maxpairwiseproduct(n,l):
    prod = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if l[i]*l[j]>prod:
                prod = l[i]*l[j]
    return prod

def maxpairwiseproductfast(n,l):
    prod = 0
    max1 = 0
    max1index = None
    for i in range(0,n):
        if l[i]>max1:
            max1 = l[i]
            max1index = i
    max2 = 0
    max2index = None
    for i in range(0,n):
        if l[i]>max2 and i!=max1index:
            max2 = l[i]
            max2index = i
    return max1*max2

n = int(input())
l = list(map(int,str(input()).split()))
# print(maxpairwiseproduct(n,l))
print(maxpairwiseproductfast(n,l))
