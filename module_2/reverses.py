str=input("enter the string:")
if len(str)%4==0:
    print(' '.join(reversed(str)))
else:
    print(str)
