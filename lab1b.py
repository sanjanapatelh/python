n=int(input("enter the number of fib numbers needed\n"))
fib=[0,1]
for i in range(n):
    if i!=0 and i!=1:
        fib.append(fib[i-1]+fib[i-2])
print("fibonacci numbers are \n")
for x in fib:
    print(x,"\t")
