x2,y2=input().split()
m2=len(x2)
n2=len(y2)
if ((n2>m2)or(n2==m2)):
    i=0
    while i<m2 and x2[i]==y2[i]:
        i+=1
    print(n2-i)
else:
    i=0
    while i<n2 and x2[i]==y2[i]:
        i+=1
    a2=x2[i:]
    b2=y2[i:]
    l2=list(a2)
    #print(l2)
    j=0
    for c2 in b2:
        if c2 in l2:
            j+=1
            l2.remove(c2)
    print(m2-i-j)
