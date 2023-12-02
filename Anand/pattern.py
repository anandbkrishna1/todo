# a=int(input("enter limit:"))
# for i in range(a):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()



def pattern():
    a=int(input("enter limit:"))
    p=0
    for i in range(1,a+1):
        for j in range(0,i):
                print("*",end=" ")
        print()
        if i%2==0:
            for j in range(1,i+1):
                print(j,end=" ")
        else:
            for j in range(i,0,-1):
                print(j,end=" ")    
        print()
pattern()