a=int(input("enter limit:"))
list1=[]
i=0
k=0
n=0
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
while k<a:
    if list1[k]%2==1:
        list3.append(list1[k])
    k+=1
while n<b:
    if list2[n]%2==0:
        list3.append(list2[n])
    n+=1
print(list3)