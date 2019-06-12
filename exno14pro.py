N,Q=map(int,input().split())
o=list(map(int,input().split()))
c=0
for i in range(0,Q):
  u,v=map(int,input().split())
  b=o[u-1:v]
  for j in b:
    c=c^j
  print(c)
  c=0
