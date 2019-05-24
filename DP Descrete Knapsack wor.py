def wightoutput(w,v,W,value):
    i = len(w)
    j = W
    out = []
    curvalue = value[i][j]
    while  curvalue!=0:

        if curvalue == value[i-1][j-w[i-1]]+v[i-1]:
            out.append(w[i-1])
            j = j-w[i-1]
        i = i-1
        curvalue = value[i][j]
    return out
def descreteknapsackwor(w,v,W):
    value = []
    out = []
    value.append([0 for _ in range(W+1)])
    for _ in range(len(w)):
        value.append([0])
    # print(value)
    for j in range(1,W+1):
        for i in range(1,len(w)+1):
            # print(i,j)
            if w[i-1]>j:
                value[i].append(value[i-1][j])
                continue
            # if value[i-1][j-w[i-1]]+v[i-1]>value[i-1][j]:
            #     out.append(w[i-1])
            #     value[i].append(value[i-1][j-w[i-1]]+v[i-1])
            # else:
            #     value[i].append(value[i-1][j])
            value[i].append(max(value[i-1][j-w[i-1]]+v[i-1],value[i-1][j]))

    # print(out)
    for i in range(len(value)):
        print(value[i])
    # print(value[len(w)][W])
    print(wightoutput(w,v,W,value))
descreteknapsackwor([6,3,4,2],[30,14,16,9],14)
