def LISoutput(l,LIS,prev):
    max = -1
    max_index = 0
    for i in range(len(LIS)):
        if max<LIS[i]:
            max = LIS[i]
            max_index = i
    out = []
    next = max_index
    while next != -1:
        out = [l[next]]+out
        next = prev[next]
    return out
def LISMemorize(l):
    LIS = []
    prev = []
    for i in range(len(l)):
        maxi = -1
        prev_max = -1
        for j in range(i):
            if l[i]>l[j]:
                if maxi<LIS[j]:
                    maxi = LIS[j]
                    prev_max = j
        prev.append(prev_max)

        if maxi == -1:
            LIS.append(1)
        else:
            LIS.append(1+maxi)
    print(l)
    print(LIS)
    print(prev)

    # for i range(len(l))
    return LISoutput(l,LIS,prev)

l = [7,2,1,3,8,4,9,1,6,9,1,2]
print(LISMemorize(l))
