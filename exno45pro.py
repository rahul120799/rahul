o=input()
if o==o[::-1]:
    print("yes")
else:
    value=o.strip("0")
    
    if value==value[::-1]:
        print("yes")
    else:
        value=o.lstrip("0")
        
        if value==value[::-1]:
            print("yes")
        else:
            print("no")
