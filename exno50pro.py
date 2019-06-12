n,m=map(int,input().split())
o=[]
for i in range(m):
  o.append(list(map(int,input().split())))
cost=10000000
f=0
for i in range(m):#loopstarts
  if o[i][0]==1:
    s=o[i][1]
    c=o[i][2]
    for j in range(i+1,m):
      if o[j][0]==s:
        s=o[j][1]
        c+=o[j][2]
    if c<cost and s==n:
      cost=c
      f+=1#loopends
if f==0:
  print(-1)
else:
  print(cost)
