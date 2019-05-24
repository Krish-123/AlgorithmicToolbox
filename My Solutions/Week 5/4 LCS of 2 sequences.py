def LCSof2(a,b):
    n = len(a)
    m = len(b)

    LCS = [[0 for _ in range(m+1)] for i in range(n+1)]
    for j in range(1,m+1):
        for i in range(1,n+1):
            if a[i-1] == b[j-1]:
                # LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1],LCS[i-1][j-1]+1)
                LCS[i][j] = LCS[i-1][j-1]+1
            else:
                LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])
    return LCS

a = input()
b = input()
LCS = LCSof2(a,b)
print(LCS[len(a)][len(b)])
