m,n=map(int,input().split())
y=[int(x)for x in input().split()]
if(n in y):
    print(n)
else:
    print(min(y))
