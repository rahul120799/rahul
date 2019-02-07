n,k=map(int,input().split())
y=[]
for i in range(n+1,k):
        if(i%2==0):
          y.append(i)   
print(*y)   
