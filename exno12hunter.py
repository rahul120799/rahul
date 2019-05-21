m,n=map(int,input().split())
lis=list(map(int,input().split()))
lis1=sorted(lis)
x=lis1[::-1]
print(x[n-1])
