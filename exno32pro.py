a5,b5=map(int,input().split())
if a5<=b5:
  d=a5
else:
  d=b5
c=[]
for i in range(0,d):
  c.append(sorted(list(map(int,input().split()))))
c=sorted(c)
for i in range(0,len(c[0])):
  for j in range(0,len(c)-1):
    if c[j][i]>c[j+1][i]:
      c[j][i],c[j+1][i]=c[j+1][i],c[j][i]
for i in c:
  print(*i)
