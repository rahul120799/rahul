import sys,string
n3 = int(input())
L = [ int(x) for x in input().split()]
n = len(L)
if n3==1 :
    print(1)
    sys.exit()
rah = 0
for i in range(1,n3-1) :
    if ((L[i] > L[i-1]) and (L[i] > L[i+1])) or ((L[i] < L[i-1]) and (L[i] < L[i+1])):
        rah += 1
print(rah)
