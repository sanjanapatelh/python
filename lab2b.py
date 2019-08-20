def rev1(str):
    lis=str.split(" ")
    lis.reverse()
    a=" "
    str1=a.join(lis)
    print(str1)

def rev2(str):
    lis=str.split(" ")
    lis2=""
    for i in lis:
        lis2+=i[::-1]
        lis2+=" "
    print(lis2)

    
str1=input("Enter the string\n")
rev1(str1)
print()
rev2(str1)
