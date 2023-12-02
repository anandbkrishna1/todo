def common():
    a=int(input("enter limit:"))
    list1=[]
    i=0
    
    while i<a:
        ele1=int(input("enter element:"))
        list1.append(ele1)
        i+=1
    print(list1)
    b=int(input("enter limit:"))
    list2=[]
    j=0
    while j<b:
        ele2=int(input("enter element:"))
        list2.append(ele2)
        j+=1
    print(list2)
    list3=[]
    for i in list1:
        for j in list2:
            if i in list2:
                if i not in list3:
                    list3.append(i)
    print(list3)
common()