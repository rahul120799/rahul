a=str(input())
A=["a","e","i","o","u"]
f=[]
d=len(a)
for i in range(0,d):
	if(a[i] in A):
		f.append(a[i])
for i in range(0,d):
	if(a[i] not in A):
		f.append(a[i])
print(*f)
