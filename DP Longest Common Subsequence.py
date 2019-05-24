def LCS(a,b,x,y):
    if x==-1 or y==-1:
        return 0
    elif a[x]==b[y]:
        return 1+LCS(a,b,x-1,y-1)
    else:
        return max(LCS(a,b,x-1,y),LCS(a,b,x,y-1))

def LCSmemorize(a,b):
    LCS = []
    LCS.append([0 for _ in range(len(b)+1)])
    for _ in range(len(a)):
        LCS.append([0])

    for j in range(1,len(b)+1):
        for i in range(1,len(a)+1):
            if a[i-1]==b[j-1]:
                LCS[i].append(LCS[i-1][j-1]+1)
            else:
                LCS[i].append(max(LCS[i-1][j],LCS[i][j-1]))
    for i in range(len(LCS)):
        print(LCS[i])
    return LCS

print(LCS('EDITING','DISTANCE',6,7))
print(LCSmemorize('EDITING','DISTANCE')[7][8])
