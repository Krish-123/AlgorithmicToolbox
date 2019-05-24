def countsort(A,M):
    C = [0 for _ in range(M)]
    for i in A:
        C[i] = C[i] + 1
    O = []
    for i in range(len(C)):
        for _ in range(C[i]):
            O.append(i)
    return O

l = [2,1,1,2,1,2,3,4,4,2,2,1,4,5,7,3,2,3,1,3,2,4,2,0,0,0,0,0]
M = 8

print(countsort(l,M))
