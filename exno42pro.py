n1,k1=map(int,input().split())
x=list(map(int,input().split()))
if k1==1:
  print(min(x))
elif k1==2:
  m=x[0]
  temp=x[0]
  for i in range(1,n1-1):
    if min(x[:i])>min(a[i+1:]):
      temp=min(x[:i])
    else:
      temp=min(x[i+1:])
    if temp>m:
      m=temp
  print(m)
else:
  print(max(x))
