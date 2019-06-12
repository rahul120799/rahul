m,n=input().split()
m=int(m)
n=int(n)
s=''
u=2
if(m+n<=3):
    for i in range(0,m+n):
        if(i%2!=0):
            s=s+'0'
        else:
            s=s+'1'
else:    
    for i in range(0,m+n):
        if(i==u):
            s=s+'0'
            if(u==b):
                u=u+2
            else:
                u=u+3
        else:
            s=s+'1'
x=len(s)-1
if(int(s[x])==0):
    print('-1')
elif m==1 and n==2: print("011")
else:
    print(s)
