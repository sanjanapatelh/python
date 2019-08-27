n = int(input("Enter the number\n"))
lis = []
for i in range(1,n+1):
    if n%i == 0:
        lis.append(i)
for i in lis:
    print(i)
