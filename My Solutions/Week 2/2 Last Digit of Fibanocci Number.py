def fiblastdigit(n):
    twostepsago = 0
    onestepago = 1
    if n<=1:
        return n
    for i in range(2,n+1):
        value = (twostepsago+onestepago)%10
        twostepsago = onestepago
        onestepago = value
    return value

print(fiblastdigit(int(input())))
