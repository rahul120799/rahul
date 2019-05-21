st3=input()
flag3=0
for i in range(0,len(st3)-1):
  for j in range(i+1,len(st3)):
    if st3[i]<st3[j]:
      flag3=1
      print(st3[j:])
      break
  if flag3==1:
    break
else:
  print(st3)
