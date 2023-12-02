# def fibanocci():
#     a=int(input("enter limit:"))
#     n1=0
#     n2=1
#     for i in range(0,a):
#         if n1<=a:
#             print(n1,end=" ")
#             n3=n1+n2
#             n1=n2
#             n2=n3
    
# fibanocci()
        
        
        
def fibanocci1():
    a=int(input("enter number:"))
    n1=0
    n2=1
    for i in range(0,a+1):
        if n1<=a:
            print(n1,end=" ")
            n3=n1+n2
            n1=n2
            n2=n3
    
fibanocci1()
        