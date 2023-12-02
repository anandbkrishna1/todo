class employee():
    def calc_slry(self):
        self.dev=int(input("enter worktime of developer in hours: "))
        self.mng=int(input("enter worktime of manager in hours:"))
class manager(employee):
    def ma_slry(self):
        self.slry=self.mng*500
        print("salary is:",self.slry)
class developer(employee):
    def de_slry(self):
        self.slry=self.dev*350
        print("salary is:",self.slry)
class main(manager,developer):
    def ma(self):
        print()
o=main()
o.calc_slry()
o.ma_slry()
o.de_slry()
        