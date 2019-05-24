def editdistance(a,b):
    ED = []
    ED.append([j for j in range(len(b)+1)])
    for i in range(1,len(a)+1):
        ED.append([i])
    for j in range(1,len(b)+1):
        for i in range(1,len(a)+1):
            if a[i-1] == b[j-1]:
                ED[i].append(min(ED[i-1][j]+1,ED[i][j-1]+1,ED[i-1][j-1]))
            else:
                ED[i].append(min(ED[i-1][j]+1,ED[i][j-1]+1,ED[i-1][j-1]+1))
    return ED

a = input()
b = input()
ED = editdistance(a,b)
# print(ED)
for i in range(len(ED)):
    print(ED[i])
print(ED[len(a)][len(b)])
