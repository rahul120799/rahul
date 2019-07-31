#GCD
n=int(input())
m=int(input())
if(n>m):
	sum=m
else:
	sum=n
for i in range(1,sum):
	if(n%i==0 and m%i==0):
		gcd=i
print(gcd)
#give inputs in next line accordingly
