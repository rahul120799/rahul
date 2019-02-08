a,z=map(int,input().split())
c=[]
for i in range(a,z):
    m=0
    y=i
    while(y>0):
        f=y%10
        f=f*f*f
        m=m+f
        y=int(y/10)
    if(m==i): 
        c.append(m)
print(*c)
