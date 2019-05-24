def fiblastdigit(n):
    f=list()
    f.append(0)
    f.append(1)
    for i in range(2,n+1):
        f.append((f[i-1]+f[i-2])%10)
    return f

def fibsumlastdigit(n):
    f = fiblastdigit(60)
    r = n%60
    sum = 0
    for i in range(0,r+1):
        sum = sum + f[i]*f[i]
        if sum>=10:
            sum = sum%10
    return (sum)
n = int(input())
print(fibsumlastdigit(n))
