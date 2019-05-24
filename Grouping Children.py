# n = int(input())
# a = list(map(int,input().split()))
n = 4
a = [1.5,1.8,2.6,3]
i = 0
tgroups = 0
while i<n:
    start = a[i]
    i+=1
    while i<n and a[i]-start<=1:
         i+=1
    tgroups+=1
print(tgroups)
