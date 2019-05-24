import random
def partition(l):
    m = 0
    c = l[0]
    for i in range(1,len(l)):
        if l[i]<=c:
            temp = l.pop(i)
            l = [temp] + l
            m = m+1
    return m,l
def quicksort(l):
    if len(l)<=1:
        return l
    m,l = partition(l)
    return quicksort(l[:m]) + [l[m]] + quicksort(l[m+1:])

def randomizedquicksort(l):
    if len(l)<=1:
        return l
    rand = random.randint(0,len(l)-1)
    temp = l.pop(rand)
    l = [temp] + l
    m,l = partition(l)
    return quicksort(l[:m]) + [l[m]] + quicksort(l[m+1:])

if __name__ == '__main__':
    l = [2,6,3,1,5,7,9,8]
    print(quicksort(l))
    l = [2,6,3,1,5,7,9,8]
    print(randomizedquicksort(l))
    # print(random.randint(0,10))
