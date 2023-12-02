def num():
    l1=[2,3,4,5,6]
    l2=[]
    for i in range(0,len(l1)):
        for j in range(0,len(l1)):
            s=l1[i]+l1[j]
            p=l1[i]*l1[j]
            if s%2==1 and p%2==0:
                pair=(l1[i],l1[j])
                m=(l1[j],l1[i])
                l2.append(pair)
                if m in l2:
                    l2.remove(m)
                
    print(l2)
num()