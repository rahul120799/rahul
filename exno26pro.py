o=int(input())
b=list(map(int,input().split()))
c=[]
a=1
for i in b:
  if i not in c:
    c.append(i)
for i in range(0,len(c)-1):
  if c[i]<c[i+1]:
    a+=1
print(a)
