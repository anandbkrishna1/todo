def fruits():
    l1=['apple','banana','cherry','date']
    l2=[]
    for i in range(0,len(l1)):
        for j in range(0,len(l1)):
            for char in l1[i]:
                if char in l1[j]:
                    p=(l1[i],l1[j])
                    l2.append(p)
                    break
    print(l2)
    
        
fruits()