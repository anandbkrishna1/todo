a=int(input("enter limit:"))

for i in range(0,a):
    for j in range(1,i+2):
        j=j+j
        print(j,end=" ")
    print()