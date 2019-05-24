def maxprizes2(n,l,nl,count):
    i = 0
    while True:
        count += 1
        if i>(len(nl)-1):
            break
        if n == (nl[i]*(nl[i]+1))/2:
            l = l+nl[i:]
            break
        if (nl[i]*(nl[i]-1))/2 < n and n < (nl[i]*(nl[i]+1))/2:
            l.append(nl[i])
            n = n-nl[i]
        i += 1
    print(count)
    return l
def maxprizes(n,l):
    nl = []
    count = 0
    for i in range(1,n+1):
        count += 1
        nl.append(i)
        if n == (i*(i+1))/2:
            l = l+nl
            return l
        if (i*(i-1))/2 < n and n < (i*(i+1))/2:
            l.append(i)
            nl = sorted(nl,reverse=True)
            return maxprizes2(n-i,l,nl[1:],count)
    return l
n = int(input())
l = []
out = maxprizes(n,l)
print(len(out),out)
