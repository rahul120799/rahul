o= int(input())
b = []
a = o//2 + o
for i in range(1,o+1):
  if i%2==0:
    b.append(i)
for i in range(1,o+1):
  if i%2!=0:
    b.append(i)
for i in range(1,o+1):
  if i%2==0:
    b.append(i)
print(a)
print(*b)
