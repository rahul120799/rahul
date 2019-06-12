o2,k1=map(int,input().split())
if o2%10==0:
  o2=str(o2)
  c=0
  for i in range(len(o2)-1,-1,-1):
    if o2[i]=='0':
      c+=1
  if k1<=c:
    print(o2)
  else:
    o2=o2[:-c]
    o2=o2+'0'*k1
    print(o2)
elif 10%(o2%10)==0:
  no=int('1'+'0'*k1)
  while True:
    if no%o2==0:
      print(no)
      break
    else:
      no+=int('1'+'0'*k1)
else:
  print(str(n2)+k1*'0')
