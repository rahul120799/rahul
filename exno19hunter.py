n,k=map(int,input().split())
z=[]
for i in range(n):
	s=set(map(int,input().split()))
	z.append(s)
f=s.intersection(*z)
print(*f)
