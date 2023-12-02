a=int(input("enter limit:"))
b=[]
i=0
l=int()
while i in range(a):
    ele=int(input("enter element:"))
    b.append(ele)
    
    i+=1
print(b)

l=b[0]

j=1
while j<a:
    if b[j]>l:
        pass
        l=b[j]
        
    j=j+1
print("largest is:",l)

   
