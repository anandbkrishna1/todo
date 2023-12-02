l1=[2,4,3]
l2=[5,6,4]
l3=[]
i=0
x=int
r=0
while i<len(l1):
    x=l1[i]+l2[i]
    x=x+r
    r=x%10
    l3.append(x)
    i+=1
print(l3)