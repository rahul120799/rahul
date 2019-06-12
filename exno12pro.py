mj,sp=map(int,input().split())
o=list(map(int,input().split()))
p=[]
for i in range(0,sp):
    b=[]
    b=list(map(int,input().split()))
    v=0
    for j in range(min(b)-1,max(b)):
        v=v+o[j]
    p.append(v)
for i in range(0,len(p)):
    print(p[i])
