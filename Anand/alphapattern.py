a=int(input("enter limit:"))
for i in range(a):
    for j in range(1,i+2):
        print(chr(65+i),end=" ")
    print()
    
a=int(input("enter limit:"))
p=chr
for i in range(0,a):
    for j in range(0,i+1):
        p=chr(65+j)
        print(p,end=" ")
    print()
    
a=int(input("enter limit:"))
p=-1
for i in range(a):
    for j in range(1,i+2):
        p+=1
        print(chr(65+p),end=" ")
    print()



a=int(input("enter limit:"))
p=chr
for i in range(a):
    print(chr(65+i),end=" ")
    for j in range(1,i+1):
        p=chr(65+i-j)
        print(p,end=" ")
    print()
    
    
