a=input("enter a password:")
up=0
lc=0
sp=0
dg=0
if len(a)>7:
    for i in a:
        if i.isupper():
            up+=1
        elif i.islower():
            lc+=1
        elif i.isdigit():
            dg+=1
        else:
            sp+=1
    if( up>0 and lc>0 and sp>0 and dg>0):
        print("STRONG")
    else:
        print("WEAK")
else:
    print("WEAK DUE TO LESS NUMBER OF CHARACTERS")
