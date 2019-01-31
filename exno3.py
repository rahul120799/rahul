A=["a","e","i","o","u"]
B=input()
if (B in A):
    print("Vowel")
elif(B.isalpha()):
    print("Consonant")
else:
    print("invalid")
