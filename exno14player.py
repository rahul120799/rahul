string = input("")
if string == 'x':
    exit();
else:
    newstr = string;
    vowels = ('a', 'e', 'i', 'o', 'u');
    for x in string.lower():
        if x in vowels:
            newstr = newstr.replace(x,"");
    F=newstr[::-1]
    print(F)
