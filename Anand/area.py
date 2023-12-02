class shape():
    def area1(self):
        self.rad=int(input("enter radius:"))
    def area2(self):
        self.l=int(input("enter length:"))
        self.w=int(input("enter width:"))
class rectangle(shape):
    def ra(self):
        self.area=self.l*self.w
        print("area:",self.area)
class circle(shape):
    def ca(self):
        self.area=3.14*self.rad*self.rad
        print("area:",self.area)
class main(rectangle,circle):
    def ma(self):
        print()
obj=main()
obj.area1()
obj.area2()
obj.ra()
obj.ca()
    

    