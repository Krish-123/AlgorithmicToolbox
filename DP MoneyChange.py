def recmoneychange(n,d):
    if n<=0:
        return 0
    min = None
    for i in range(len(d)):
        if d[i]>n:
            continue
        ans = recmoneychange(n-d[i],d)+1
        if min is None or ans < min:
            min = ans
    # print(ans)

    return min
def monechangedp(n,d):
    l = [0]
    for i in range(1,n+1):
        min = None
        for j in range(len(d)):
            if i<d[j]:
                continue
            if min is None or l[i-d[j]]<min:
                min = l[i-d[j]]+1
        l.append(min)
    return l[n]

n = int(input())
d = [1,8,20]
print(monechangedp(n,d))
# print(recmoneychange(n,d))
