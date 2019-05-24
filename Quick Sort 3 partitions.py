import random
def partition3(l):
    m1 = 0
    m2 = 0
    c = l[0]
    for i in range(1,len(l)):
        if l[i]<c:
            temp = l.pop(i)
            l = [temp] + l
            m1 = m1+1
        elif l[i]==c:
            temp = l.pop(i)
            l = l[:m1] + [temp] + l[m1:]
            m2 = m2+1
    m2 = m1 + m2
    return m1,m2,l

def randomizedquicksort3(l):
    if len(l)<=1:
        return l
    rand = random.randint(0,len(l)-1)
    temp = l.pop(rand)
    print(temp)
    l = [temp] + l
    m1,m2,l = partition3(l)
    print(m1,m2,l)
    return randomizedquicksort3(l[:m1]) + l[m1:m2+1] + randomizedquicksort3(l[m2+1:])

if __name__ == '__main__':
    l = [2,6,3,1,5,7,9,8,2,2,2,1,1,2,1,2,1,3,3,1,2,1,3,1,3,1,7,5,2,6,6,4,6,8,3,4,6,7,3,6,7,4,3,5,7,3,2,5]
    print(randomizedquicksort3(l))
