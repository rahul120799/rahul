a=input()
y=''
m=0
i=0
while i<len(a)-1:
  if a[i]=='a' and a[i+1]=='b':
    y+=a[i]+a[i+1]
    i+=2
  else:
    y=''
    i+=1
  if m<len(y):
    m=len(y)
b=len(a)-1
if a[b]=='a' and a[b-1]=='b' and y!='':
  m+=1
print(m)
