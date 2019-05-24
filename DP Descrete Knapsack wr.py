def optimalweightsoutput(weights,prev_u):
    last = weights[-1]
    prev = prev_u[-1]
    out = []
    while prev != -1:
        out.append(last)
        last = weights[prev]
        prev = prev_u[prev]
    return out
def descreteknapsack(w,v,W):

    weights = []
    prev_u = []
    value = []
    for u in range(W+1):
        if u == 0:
            value.append(0)
            weights.append(0)
            prev_u.append(-1)
            continue
        maxvalue = 0
        weight = 0
        prev = -1
        for i in range(len(w)):
            if w[i]>u:
                continue
            if maxvalue<(value[u-w[i]]+v[i]):
                maxvalue = value[u-w[i]]+v[i]
                weight = w[i]
                prev = u-w[i]

        weights.append(weight)
        prev_u.append(prev)
        value.append(maxvalue)
    print(max(value))
    print(optimalweightsoutput(weights,prev_u))

descreteknapsack([6,3,4,2],[30,14,16,9],22)
