a=int(input("enter limit:"))
i=0
b=[]
c=[]
while i in range(a):
    ele=str(input("enter element:"))
    b.append(ele)
    if len(ele)>5:
        c.append(b[i])
    i+=1
print(c)