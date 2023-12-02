# a=int(input("enter limit:"))
# p=-1
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         p+=2
#         print(p,end=" ")
#     print()
    
    
a=int(input("enter limit:"))
for i in range(a):
    for j in range(1,i+2):
        if i%2==0:
            print("*",end=" ")
            print(j,end=" ")
        else:
            print("*",end=" ")
            print(i-1,end=" ")
    print()
    
