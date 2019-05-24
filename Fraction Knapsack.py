
def fracknapsack(w,v,W):

    V = list()
    A = list()
    for i in range(len(w)):
        if W == 0:
            return V,A
        if w[i]<=W:
            V.append(v[i])
            A.append(w[i])
            W = W-w[i]
        else:
            V.append((float(v[i])/w[i])*W)
            A.append((float(V[i])/v[i])*w[i])
            W = W-A[i]
    return V,A

#Input should be sorted using the v/w ratio
print(fracknapsack([2,3,4],[14,18,20],7))
