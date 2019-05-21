n,k=map(int,input().split())
f= [[abs(i-k),i]for i in [int(x) for x in input().split()]]
f.sort()
f=f[1:]
f=[i[1] for i in f[:3]]
print(*f)
