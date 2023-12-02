def square():
    a=int(input("enter limit:"))
    b=[]
    sum=0
    for i in range(a):
        ele=int(input("enter element:"))
        b.append(ele)
    print(b)
    for i in range(len(b)):
        sum=sum+b[i]**2
    print(sum)
square()