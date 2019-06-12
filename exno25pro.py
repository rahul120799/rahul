o=int(input())
l=list(map(int,input().split()))
m=[]
a=1
for i in range(n-1):
	if l[i]<l[i+1]:
		a+=1
	else:
		m.append(a)
		a=1
m.append(a)
print(max(m))
