def merge(a,b,I1,I2,out1,out2):
    if len(a) == 0:
        out1 = out1+b
        out2 = out2+I2
        return out1,out2
    if len(b) == 0:
        out1 = out1+a
        out2 = out2+I1
        return out1,out2
    if a[0]<=b[0]:
        out1.append(a[0])
        out2.append(I1[0])
        return merge(a[1:],b,I1[1:],I2,out1,out2)
    else:
        out1.append(b[0])
        out2.append(I2[0])
        return merge(a,b[1:],I1,I2[1:],out1,out2)
def mergesort(l,I):
    if len(l) <= 1:
        return l,I
    m = len(l)/2
    a,I1 = mergesort(l[:m],I[:m])
    b,I2 = mergesort(l[m:],I[m:])
    out1 = []
    out2 = []
    l,I = merge(a,b,I1,I2,out1,out2)
    return l,I
def distance(p1,p2):
    # print(p1,p2)
    # print('Individual')
    # print(abs(p1[0]-p2[0])**2,abs(p1[1]-p2[1])**2)
    # print(float(abs(p1[0]-p2[0])**2+abs(p1[1]-p2[1])**2)**(0.5))
    return float(abs(p1[0]-p2[0])**2+abs(p1[1]-p2[1])**2)**(0.5)
def middleband(l,d):
    if len(l)<=1:
        return d
    dmin = None
    for i in range(len(l)):
        if i+7<=len(l)-1:
            c = i+7
        else:
            c = len(l)-1
        for j in range(i+1,c+1):
            dcur = distance(l[i],l[j])
            if dmin is None:
                dmin = dcur
            elif dmin>dcur:
                dmin = dcur
    return min(dmin,d)
def closestpoints(p,x,y,I1,I2,low,high):
    # print(low,high)
    if low>=high :
        print -1
        # return -1
    if high-low == 1:
        # print(distance(p[I1[low]],p[I1[high]]))
        return distance(p[I1[low]],p[I1[high]])
    m = low+(high-low)/2
    # print('First')
    d1 = closestpoints(p,x,y,I1,I2,low,m-1)
    # print('Second')
    d2 = closestpoints(p,x,y,I1,I2,m,high)
    # if d1 == -1 and d2 == -1:
    #     return distance(p[low],p[low+1])
    if d1 == -1:
        d = d2
    elif d2 == -1:
        d = d1
    else:
        d = min(d1,d2)
    # l = [[x[i],p[I1[i]][1]] for i in range(len(x)) if abs(x[i]-x[m])<=d]
    # print(d)
    l = [[p[I2[i]][0],y[i]] for i in range(len(y)) if abs(p[I2[i]][0]-x[m])<=d]
    # print(l)
    d = middleband(l,d)
    # print(d)
    # print(d,d1,d2)
    return d

# p = [[4,4],[-2,-2],[-3,-4],[-1,3],[2,3],[-4,0],[1,1],[-1,-1],[3,-1],[-4,2],[-2,4]]
# p = [[7,7],[1,100],[4,8],[7,7]]
p = [[0,0],[3,4]]

x = [i for i,j in p]
y = [j for i,j in p]
I = [i for i in range(len(p))]
x,I1 = mergesort(x,I)
y,I2 = mergesort(y,I)
# print(x,I1,y,I2)
ans = closestpoints(p,x,y,I1,I2,0,len(p)-1)
# print(ans)
print("%0.4f" % ans)
