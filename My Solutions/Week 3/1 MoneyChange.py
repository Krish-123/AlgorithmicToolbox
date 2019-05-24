def moneychange(n):
    tc = 0
    for i in [10,5,1]:
        tc = tc + n/i
        n = n%i
    return tc

n = int(input())
print(moneychange(n))
