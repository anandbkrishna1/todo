def factorial():
    a=int(input("enter number:"))
    fact=1
    while a>=1:
        fact=fact*a
        a-=1
    print(fact)
factorial()
    