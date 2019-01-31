A=["a","e","i","o","u"]
B=input()
if (B in A):
    print("vowel")
elif(B.isalpha()):
    print("Consonant")
else:
    print("invalid")
