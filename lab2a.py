def search(lis,a):
    if a in lis:
        return True
    else:
        return False

lis=[]
while True:
    a=int(input("Enter the elemets\n"))
    if a!=-1:
        lis.append(a)
    else:
        break
b=int(input("Enter the element to be searched\n"))
if(search(lis,b)):
    print(b," is present in list")
else:
    print(b," is not present in list")
