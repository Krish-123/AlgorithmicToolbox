def editdistance(a,b):
    D = []
    for j in range(len(b)+1):
        for i in range(len(a)+1):
            if i==0 and j==0:
                D.append([i])
                continue
            elif i==0:
                D[i].append(j)
                continue
            elif j==0:
                D.append([i])
                continue
            inse = D[i-1][j]+1
            dele = D[i][j-1]+1
            mism = D[i-1][j-1]+1
            matc = D[i-1][j-1]
            # print(i,j)
            if a[i-1] == b[j-1]:
                D[i].append(min(inse,dele,matc))
            else:
                D[i].append(min(inse,dele,mism))
    for i in range(len(D)):
        print(D[i])
    print(D[len(a)][len(b)])

# editdistance('EDITING','DISTANCE')
editdistance('REALLY','BREAD')
