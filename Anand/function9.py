def sum():
    l1=[3,8,12,7,6,10,21,15]
    l2=[]
    
    for i in range(0,len(l1)):
        for j in range(1,len(l1)):
            if l1[i]+l1[j]==18:
                n=(l1[i],l1[j])
                m=(l1[j],l1[i])
                l2.append(n)
                if m in l2:
                    l2.remove(m)
                
    print(l2)             
        
               
sum()
        