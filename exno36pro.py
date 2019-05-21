import sys,string
num2 = int(input())
M = [ int(x) for x in input().split()]
num2 = len(M)
rah = 0
for i in range(0,num2-2) :
    for j in range(i+1, num2-1):
        for k in range(j+1, num2):
            if M[i] > M[j] > M[k] :
                rah += 1
print(rah)
