i=1
while i!=-1:
    x=int(input("enter the number:"))
    if x>0:
        print( "The number ",x," is positive")
    elif x<0:
        print ("The number ",x," is negative")
    else:
        print ("The number is zero")
    i=int(input("enter -1 to exit and 1 to continue\n"))
