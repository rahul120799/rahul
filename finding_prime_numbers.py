#to check prime numbers
n=int(input())
if(n>1):
	for i in range(2,n):
		if(n%i==0):
			print("not a prime number")
			break
	else:
		print("prime number")
else:
	print("not a prime number")
#note that else should be outside because when break executes it comes out of loop
