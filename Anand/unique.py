a=int(input("enter limit:"))
b=[]
c=[]
i=0
while i<a:
    ele=str(input("enter element:"))
    b.append(ele)
    i+=1
print(b)
for i in b:
    if i not in c:
        c.append(i)
print("unique elements:",c)
     

    