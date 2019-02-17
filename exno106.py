n,k=map(int,input().split())
a=[int(x) for x in input().split()]
x=a[k]
if(x%2==1):
    print(x)
else:
    y=a[k-1]
    print(y)
