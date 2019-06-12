o=int(input())
i=0
x=0
b=[]
while i<90 and i<o:
  r=0
  for j in str(o-i):
    r+=int(j)
  if r+(o-i)==o:
    x+=1
    b.append(o-i)
  i+=1
print(x)
for i in b:
  print(i)
