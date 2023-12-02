def square():
    a=int(input("enter limit:"))
    b=[]
    for i in range(a):
        ele=int(input("enter element:"))
        b.append(ele)
    print(b)
    for i in range(len(b)):
        b[i]=b[i]**2
    print(b)
square()
    