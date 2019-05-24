import random
def partition(l):
    m1,m2 = 0,0
    p = l[0]
    for i in range(1,len(l)):
        if l[i]<p:
             t = l.pop(i)
             l = [t]+l
             m1 = m1+1
             m2 = m2+1
        elif l[i]==p:
            temp = l[i]
            l[i] = l[m2+1]
            l[m2+1] = temp
            m2 = m2+1
    return m1,m2,l
def quicksort(l):
    if len(l)<=1:
        return l
    rand = random.randint(0,len(l)-1)
    temp = l[rand]
    l[rand] = l[0]
    l[0] = temp
    m1,m2,l = partition(l)
    return quicksort(l[:m1])+l[m1:m2+1]+quicksort(l[m2+1:])

n = int(input())
l = map(int,input().split())
print(quicksort(l))
