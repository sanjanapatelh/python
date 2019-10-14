dic={'(':')','[':']','{':'}'}
input_string=input("enter the string:\n")
lis=list(input_string)
l=[]
x=len(lis)-1
i=0
while x!=0 and len(lis)!=0 and i<x:
    if lis[i] in dic.keys():
        if dic[lis[i]]==lis[i+1]:
            del(lis[i])
            del(lis[i])
            x=x-1
        else:
            l.append(lis[i])
            i=i+1
            x=x-1
    else:
        if dic[l.pop()]==lis[i]:
            del(lis[i])
            del(lis[i-1])
            i=i-1
            x=x-1
        else:
            x=0
        
if len(l)==0:
    print("valid string")
else:
    print("invalid string")
		
        
     
	
