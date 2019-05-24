import random
def isgreatorequal(a,max):
    if int(str(max)+str(a)) > int(str(a)+str(max)):
        return False
    else:
        return True

def MaxSalary(l):
    out = ''
    while l != []:
        max = 0
        maxindex = 0
        for i in range(len(l)):
            if isgreatorequal(l[i],max):
                max = l[i]
                maxindex = i
        out = out+str(l.pop(maxindex))
    return out

l = [23,39,92]
n = random.randint(1,100)
l = [random.randint(0,1000) for i in range(n)]
print(MaxSalary(l))
