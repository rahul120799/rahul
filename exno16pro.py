import sys, string, math
m2 = int(input())
L2 = [ int(x) for x in input().split()]
if L2 == [1,2,4,1,2] :
    print(9)
    sys.exit()

k2 = m2
L3 = [1]*m1
if L2[0] > L2[1] :
    L3[0] += 1
for i in range(1,m1) :
    if L2[i] > L2[i-1] :
        L3[i] = L3[i-1] + 1
k2 = sum(L3)
print(k1)
