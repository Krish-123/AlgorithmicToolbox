def GCD(a,b):
    d = 0
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            d = i
    return d

def gcdfast(a,b):
    if b == 0:
        return a
    r = max(a,b)%min(a,b)
    return gcdfast(min(a,b),r)

a,b = map(int,str(input()).split())
print(gcdfast(a,b))
