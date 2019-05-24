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


n = int(input())
d = [1,8,20]
print(recmoneychange(n,d))
