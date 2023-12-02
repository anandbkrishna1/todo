a=int(input("enter limit:"))
p=0
for i in range(1,a+1):
    for j in range(1,i+1):
        p+=2
        print(p,end=" ")
    print()