o= input()
u = input()
c = o.split('|')
if len(c[0]+u)==len(c[1]):
  print(c[0]+u+'|'+c[1])
elif len(c[0])==len(c[1]+u):
  print(c[0]+'|'+c[1]+u)
else:
  print("Impossible")
