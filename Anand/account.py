class bankacc():
    def __init__(self):
        self.name="amal"
        self.savbal=1000
        self.chkbal=0
        self.depbal=0
    def dep(self):
        self.depo=int(input("enter amount :"))
        print("1.savingsaccount")
        print("2.checkingaccount")
        a=int(input("enter option:"))
        if a==1:
            self.savbal=self.savbal+self.depo
        elif a==2:
            self.chkbal=self.chkbal+self.depo
        else:
            print("error")
    def wit(self):
        self.depo=int(input("enter amount :"))
        print("1.savingsaccount")
        print("2.checkingaccount")
        a=int(input("enter option:"))
        if a==1:
            self.savbal=self.savbal-self.depo
        elif a==2:
            self.chkbal=self.chkbal-self.depo
        else:
            print("error")
        
        