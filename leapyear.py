#leap year
a=int(input())
if(a%4==0 and a%100!=0 or a%400==0):
	print("it is a leap year")
else:
	print("not a leap yeap year")
	
# and or should come inside the bracket 
