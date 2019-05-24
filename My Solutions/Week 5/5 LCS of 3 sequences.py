def LCSof3(a,b,c):
    n = len(a)
    m = len(b)
    l = len(c)

    LCS = [[[0 for _ in range(l+1)] for i in range(m+1)] for j in range(n+1)]
    for k in range(1,l+1):
        for j in range(1,m+1):
            for i in range(1,n+1):
                if a[i-1] == b[j-1] == c[k-1]:
                    # print('yes')
                    LCS[i][j][k] = LCS[i-1][j-1][k-1]+1
                else:
                    LCS[i][j][k] = max(LCS[i-1][j][k],LCS[i][j-1][k],LCS[i][j][k-1])
    return LCS

a = input()
b = input()
c = input()
LCS = LCSof3(a,b,c)
print(LCS)
print(LCS[len(a)][len(b)][len(c)])
