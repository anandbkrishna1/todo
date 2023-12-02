a=int(input("enter limit:"))
b=[]
c=[]
i=0
while i in range(a):
    ele=int(input("enter element:"))
    b.append(ele)
    if(b[i]%2==0):
        c.append(b[i])
    i+=1
print("list of even no:",c)