n=int(input())
u=n
t=0
while(u>0):
    c=u%10
    c=c*c*c
    t=t+c
    u=int(u/10)
if(t==n):
    print("yes")
else:
    print("no")
