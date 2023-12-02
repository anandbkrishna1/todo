# while True:
#     a=int(input("enter choice:"))
#     if a==1:# class Bank():
#     def __init__(self):
#         self.num=1
#         self.name="amal"
#         self.bal=1000
#     def withdraw(self):
#         n=int(input("enter amount to withdraw:"))
#         self.bal=self.bal-n
#     def deposit(self):
#         n=int(input("enter amount to deposit:"))
#         self.bal=self.bal+n
#     def show(self):
#         print(self.num)
#         print(self.name)
#         print(self.bal)
        
  
# obj=Bank()   

#         obj.show()
#     elif a==2:
#         obj.withdraw()
#     elif a==3:
#         obj.deposit()
#     elif a==4:
#         break
#     else:
#         print("wrong choice")
        
        
        
        
class Bank():
    def __init__(self,num,name,bal):
        self.num=num
        self.name=name
        self.bal=bal
    def withdraw(self):
        n=int(input("enter amount to withdraw:"))
        self.bal=self.bal-n
    def deposit(self):
        n=int(input("enter amount to deposit:"))
        self.bal=self.bal+n
    def show(self):
        print(self.num)
        print(self.name)
        print(self.bal)
list=[]  
while True:
    a=int(input("enter choice:"))
    if a==1:
        num=int(input("enter account number:"))
        name=(input("enter name:"))
        bal=int(input("enter balance:"))
        x=Bank(num,name,bal)
        list.append(x)
    elif a==2:
        acc=int(input("enter account no:"))
        for i in list:
            if (i.num==acc):
                i.deposit()
            else:
                print("no such account")
    elif a==3:
        acc=int(input("enter account no:"))
        for i in list:
            if( i.num==acc):
                i.withdraw()
            else:
                print("no such account")
    elif a==4:
        acc=int(input("enter account no:"))
        for i in list:
            if (i.num==acc):
                i.show()   
            else:
                print("no such account") 
    elif a==5:
        for i in list:
            print("Accout no:",i.num)
            print("Account name:",i.name)
            print("Account balance:",i.bal) 
            print("___________________")
    elif a==5:
        print("Exit")
        break
    else:
        print("WRONG CHOICE")
        
        
        
        
        