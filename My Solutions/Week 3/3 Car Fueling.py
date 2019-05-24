def refuelcount(m,S,d):

    S = [0] + S + [d]
    refill = 0
    r = m
    for i in range(len(S)-1):
        if S[i+1]-S[i]>m:
            return -1
        if S[i+1]-S[i]<=r:
            r = r - (S[i+1]-S[i])
        else:
            refill += 1
            r = m - (S[i+1]-S[i])
    return refill

d = int(input())
m = int(input())
n = int(input())
S = list(map(int,input().split()))

# d = 10
# m = 3
# n = 4
# S = [1,2,5,9]

print(refuelcount(m,S,d))
