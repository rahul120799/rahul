o=input()
m=0
l=[]
for i in range(0,len(o)-1):
    for j in range(i+1,len(o)):
        s=t[i:j+1]
        k=s[::-1]
        if s==k:
            l.append(len(o)-len(k))
print(min(l))
