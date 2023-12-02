a=int(input("enter limit"))
list1=[]
i=0
while i<a:
    ele1=int(input("enter element:"))
    list1.append(ele1)
    i+=1
print(list1)
b=int(input("enter choice:"))
for b in list1:
    for i in range(len(list1)):
        