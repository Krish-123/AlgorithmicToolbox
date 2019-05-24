def GCD(a,b):
    if b==0:
        return a
    else:
        r = max(a,b)%min(a,b)
        return GCD(min(a,b),r)

a,b = input().split()
print(GCD(int(a),int(b)))
