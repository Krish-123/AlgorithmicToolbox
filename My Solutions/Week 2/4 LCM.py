import random
def GCD(a,b):
    if b==0:
        return a
    else:
        r = max(a,b)%min(a,b)
        return GCD(min(a,b),r)
def LCMNaive(a,b):
    i = 0
    l1 = list()
    l2 = list()
    p = min(a,b)
    q = max(a,b)
    while True:
        i+=1
        m1 = p*i
        m2 = q*i
        l1.append(m1)
        l2.append(m2)
        if m1 in l2:
            return m1

def LCM(a,b):
    return a*b/GCD(a,b)

def stresstest():
    while True:
        a = random.randint(1,2000000000)
        b = random.randint(1,2000000000)
        print(LCM(a,b))
        # if LCMNaive(a,b) == LCM(a,b):
        #     print("True")
        # else:
        #     print(LCMNaive(a,b))
        #     print(LCM(a,b))
        #     print(a,b)
        #     break

a,b = map(int,input().split())
print(LCM(a,b))
# stresstest()
