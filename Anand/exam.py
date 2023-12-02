# a=int(input("enter limit:"))
# for i in range(0,a):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

a=int(input("enter limit:"))
# b=str(input("enter character:"))
for i in range(a):
    p=chr(65+i)
    print(p,end=" ")
    # if p==b:
    #     break