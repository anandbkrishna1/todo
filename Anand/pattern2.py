# a=int(input("enter limit:"))

# for i in range( 0,a):
#     for j in range(0,a-i):
#         print("*" ,end=" ")
#     print()



# a=int(input("enter limit:"))

# for i in range(a,-1,-1):
#     for j in range(i+1):
#         if j==0 or j==i or i==a:
#             print("*" ,end=" ")
#         else:
#             print(" ",end=" ")
#     print()


n=int(input("enter limit:"))
for i in range(n):
    for j in range(n,i+1,-1):
        print(" ",end="")
    for j in range(2*i+1):
        if j==0 or j==2*i:
            print("*",end="")
        elif i==2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
