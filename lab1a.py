n=int(input("enter the number of elements to be in list\n"))
list1=[];
for i in range(n):
    ele=int(input("enter the element\n"))
    list1.append(ele)
list2=[];
for i in range(n):
    if list1[i]%2==0:
        list2.append(list1[i])
for x in list2:
    print(x,"\t")
