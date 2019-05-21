s14,s24=input().split()
s1=0
if len(s14)>len(s24):
  s14,s24=s24,s14
i=0
while i<len(s14):
  s1+=(ord(s24[i])-ord(s14[i]))
  i+=1
for i in range(i,len(s24)):
  s1+=ord(s24[i])-ord('a')+1
print(s1)
