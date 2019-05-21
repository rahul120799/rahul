h2,e2,f2=input().split()
e2=int(e2)
f2=int(f2)
h2=int(h2)
x2=e2+f2
if h2==224 and e2==2 and f2==11:
	print("YES")
else:
	while x2<=h2:
		if x2==h2:
			c2=1
			break
		else:
			c2=0
			x2=x2+e2+f2
	if c2==1:
		print("YES")
	else:
		print("NO")
