def collectingsigns(l):
    i = 0
    minpoints = 0
    b = []
    while True:
        a1 = l[i][0]
        b1 = l[i][1]
        i = i+1
        if i > len(l)-1:
            minpoints += 1
            b.append(b1)
            break
        while True:
            a2 = l[i][0]
            b2 = l[i][1]
            if b1>=a2:
                i+=1
                if i > len(l)-1:
                    minpoints += 1
                    b.append(b1)
                    break
            else:
                minpoints += 1
                b.append(b1)
                break

        if i > len(l)-1:
            break
    return minpoints,b

# n = int(input())
# l = []
# for i in range(n):
#     l.append(list(map(int,input().split())))
# l = [[2,4],[2,5],[3,4],[3,7],[8,10],[9,11],[12,14],[13,16]]
l = [[2,5],[4,6],[2,4],[7,8],[3,6],[1,3]]
l = sorted(l,key = lambda t:(t[0],t[1]))
print(collectingsigns(l))
