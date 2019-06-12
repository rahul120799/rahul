o,k=map(int,input().split())
a=list(map(int,input().split()))
b=a[:]
c=0
s=0
for i in a:
    b.remove(i)
    for j in b:
        if(s==0):
            if(i+j==k):
                print("yes")
                c=c+1
                s=s+1
    b=a[:]
if(c==0):
    print("no")
