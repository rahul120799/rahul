o=input()
flag=0
for i in range(1,len(o)):
  j=0
  while j<len(o) and len(o[:j]+o[i+j:])==len(o)-i:
    n=o[:j]+o[j+i:]
    if int(n)%8==0:
      flag=1
      print('yes')
      break
    j+=1
  if flag==1:
      break
else:
  print('no')
