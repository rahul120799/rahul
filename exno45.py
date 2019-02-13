x=input()
y=len(x)
count=0
for i in range(0,y):
   if(x[i].isnumeric()):
       count=count+1
print(count)
