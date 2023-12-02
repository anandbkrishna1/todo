# def sum():
#     l1=[4,8,7,3]
#     num=10
#     l2=[]
#     l4=[]
#     l3=[4,9,1,2]
#     for i in range(0,len(l1)):
#         for j in range(1,len(l1)):
#             if l1[i]+l1[j]==num:
#                 n=i
#                 # m=j,i
#                 l2.append(n)
#                 # if n in l2:
#                 #     l2.remove(n)
#     print("position of elements:",l2)
#     for i in range(0,len(l3)):
#         for j in range(1,len(l3)):
#             if l3[i]+l3[j]==num:
#                 k=i
#                 # x=j,i
#                 l4.append(i)
#                 # if k in l4:
#                 #     l4.remove(k)
#     print("position of elements:",l4)
                                        
# sum()


def sum():
    # l1=[4,8,7,3]
    num=10
    # l3=[4,9,1,2]
    a=int(input("enter limit:"))
    l1=[]
    for i in range(a):
        ele=int(input("enter elements:"))
        l1.append(ele)
    # print(l1)
    
    b=int(input("enter limit:"))
    l3=[]
    for j in range(b):
        ele=int(input("enter element:"))
        l3.append(ele)
    # print(l3)
    
    c=int(input("enter limit:"))
    l4=[]
    for k in range(c):
        ele=int(input("enter element:"))
        l4.append(ele)
    print(l1)
    print(l3)
    print(l4)
    for i in range(0,len(l1)):
        for j in range(0,len(l3)):
            for k in range(0,len(l4)):
                if l1[i]+l3[j]+l4[k]==num:
                    n=(i,j,k)    if l1[i]+l3[j]+l4[k]==num:
                    n=(i,j,k)
                    print(n)
                    print(n)
    
sum()
        
        