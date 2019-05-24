x=int(input())
b=list(map(int,input().split()))
y=[]
for i in range (0,x):
  if i==0:
    p=1
    d=b[i+1:]
    for i in d:
      p=p*i
    y.append(p)
  elif i==x-1:
    p=1
    d=b[:i]
    for i in d:
      p=p*i
    y.append(p)
  else:
    s1,s2=b[:i],b[i+1:]
    p1,p2=1,1
    for i in s1:
      p1=p1*i
    for i in s2:
      p2=p2*i
    y.append(p1*p2)
print(*y)
