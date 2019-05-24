z,k=map(int,input().split())
x=[]
l1=[]
for i in range(z):
    l=[int(x) for x in input().split()]
    x.append(l)
    if 0 in l:
        y=l.index(0)
        l1.append(y)
for i in range(len(x)):
    if 0 in x[i]:
        for j in range(k):
            x[i][j]=0
for i in l1:
    for j in range(n):
        x[j][i]=0
for i in x:
    print(*i)
