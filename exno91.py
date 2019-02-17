L,W,H=map(int,input().split())
v=L*H*W
sa=2*(L*W) + 2*(W*H) + 2*(L*H)
print(sa,v)
