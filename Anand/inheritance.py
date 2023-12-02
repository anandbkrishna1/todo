# class a:
#     def hey(self):
#         print("hello")
# class b(a):
#     def hlo(self):
#         super().hey()
#         print("how are you")
# class c(a):
#     def hii(self):
#         super().hlo()
#         print("hope u r fine")
# obj=c()
# obj.hii()



class animals():
    def anmls(self):
        print("ANIMALS")
class mammals(animals):
    def mamls(self):
        super().anmls()
        print("MAMMALS")
class birds(mammals):
    def brd(self):
        super().mamls()
        print("BIRDS")
class fish(birds):
    def fsh(self):
        super().brd()
        print("FISH")
obj=fish()
obj.fsh()
        
                



        