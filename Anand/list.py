a=list(input("enter list1:"))
b=list(input("enter list2:"))

c=[]
i=0
j=0
while i<len(a) and j<len(b):
    
    if a[i]==b[j]:
        c.append(a[i])
        i+=1
        j+=1
    # elif a[i]<b[j]:
    #     i+=1
    else:
        i+=1  
    # else:
    #     print("no common elements found")     
print("list is:",c)
    
        
        
        