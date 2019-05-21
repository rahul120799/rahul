x=int(input())
S=str(x)
y=0
for i in range(0,len(S)):
    if int(S[i:i+2])<26 and len(str(int(S[i:i+2])))==2:
        y=y+1
if y==2:
    print(y+y//2)
else:
    print(y+y//2+1)
