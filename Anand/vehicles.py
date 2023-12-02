l=[]
class vehicle:
    def ve(self):
        self.name=str(input("enter the name of the vehicle: "))
        self.year=int(input("enter the year of made: "))
        self.color=str(input("enter the color: "))
        l.append(self.name)
        l.append(self.year)
        l.append(self.color)
class car(vehicle):
    def ca(self):
        self.make=str(input("enter the brand name: "))
        self.model=str(input("enter the model name: "))
        l.append(self.make)
        l.append(self.model)
class truck(vehicle):
    def tr(self):
        self.bed_length=int(input("enter the bed_length: "))
        self.payload_capacity =int(input("enter the payload_capacity: "))
        l.append(self.bed_length)
        l.append(self.payload_capacity)
class main(car,truck):
    def ma(self):
        print("name: ",l[0]," ,year: ",l[1]," ,color: ",l[2]," ,brand: ",l[3]," ,model: ",l[4]," ,bed_length: ",l[5]," ,payload_capacity: ",l[6])
obj=main()
obj.ve()
obj.ca()
obj.tr()
obj.ma()
