a=input()
b=len(a)
count=0
for i in range(0,b):
   if(a[i].isnumeric()):
       count=count+1
print(count)
