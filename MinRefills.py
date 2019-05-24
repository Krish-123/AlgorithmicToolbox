


# n = int(input())
# x = list(map(int,str(input()).split()))
# l = int(input())

n = 5
x = [0,150,275,400,575,800,900]
l = 300

numrefills = 0
curstation = 0
lastrefill = 0
while curstation<=n:
    lastrefill = curstation

    while curstation<=n and x[curstation+1]-x[lastrefill]<=l:
        curstation+=1
        print(curstation)
    if curstation == lastrefill:
        print("impossible")
    if curstation<=n:
        numrefills+=1
print(numrefills)
