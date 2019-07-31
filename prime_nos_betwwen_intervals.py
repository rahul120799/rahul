#to check prime numbers between interval
n=int(input())
m=int(input())
for c in range(n+1,m):
	if(c>1):
		for i in range(2,c):
			if(c%i==0):
				break
		else:
			print(c,end=' ')
#note that else should be outside because when break executes it comes out of loop
