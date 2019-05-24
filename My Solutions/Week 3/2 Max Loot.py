def fracknapsack(n,W,v,w,vw,totalval=0):

    for i in range(n):
        max_index = vw.index(max(vw))
        if w[max_index] < W:
            totalval = totalval + v[max_index]
            W = W - w[max_index]
        else:
            totalval = totalval + W*vw[max_index]
            return totalval
        w.pop(max_index)
        v.pop(max_index)
        vw.pop(max_index)
    return totalval

n,W = map(int,input().split())
w = [0 for _ in range(n)]
v = [0 for _ in range(n)]
vw = list()

for i in range(n):
    v[i],w[i] = map(int,input().split())
    vw.append(float(v[i])/w[i])
print("%.4f" %fracknapsack(n,W,v,w,vw))
