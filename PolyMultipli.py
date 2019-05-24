def multipolynaive(a,b):
    prod = [0 for i in range(2*len(a)-1)]
    for i in range(len(a)):
        for j in range(len(b)):
            prod[i+j]=prod[i+j]+a[i]*b[j]
    return prod

def multipolyDnCnaive(a,b):
    # print(a,b)
    if len(a)==1 and len(b)==1:
        # print(a[0]*b[0])
        return([a[0]*b[0]])
    mid = (len(a)/2)-1

    res = multipolyDnCnaive(a[:mid+1],b[:mid+1])+[i+j for i in multipolyDnCnaive(a[:mid+1],b[mid+1:]) for j in multipolyDnCnaive(a[mid+1:],b[:mid+1])]+multipolyDnCnaive(a[mid+1:],b[mid+1:])
    print(res)
    return(res)

print(multipolynaive([0,3,2,5],[0,5,1,2]))
print(multipolyDnCnaive([0,3,2,5],[0,5,1,2]))
