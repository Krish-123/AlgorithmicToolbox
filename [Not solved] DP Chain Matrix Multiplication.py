def CMM(A):
    n = len(A)
    m = []
    for i in range(n):
        m.append(len(A[i]))
    m.append(len(A[-1][-1]))
    print(m)
    # # M = [[0]*(n+1)]*n
    # M = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    M = [[0 for _ in range(n+1)] for _ in range(n)]
    # print M
    for i in range(n):
        for j in range(i+1,n+1):
            if j == i+1:
                continue
            minele = None
            for k in range(i+1,j):
                ele = M[i][k] + M[k][j] + m[i]*m[k]*m[j]
                if minele is None or ele<minele:
                    minele = ele
            M[i][j] = minele

    print M


A = [[[1,2],[3,4]],[[5,6,7],[8,9,10]],[[11,12,13],[14,15,16],[17,18,19]],[[20,21,22,23],[24,25,26,27],[28,29,30,31]]]
CMM(A)
