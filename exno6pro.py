s1=int(input())
n1=input().split()
d1=0
for i in range(0,len(n1)):
   n1.insert(i,int(n1[i]))
   n1.remove(n1[i+1])
for i in range(0,len(n1)-2):
   for j in range(1,len(n1)-1):
      for k in range(2,len(n1)):
          if(n1[i]<n1[j]<n1[k])and(i<j<k):
             d1=d1+1

print(d1)
