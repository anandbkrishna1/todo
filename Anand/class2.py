# class circle():
#     def __init__(cir):
#         cir.radius=int(input("enter radius in cm:"))
#     def area(cir):
#         Area=3.14*cir.radius*cir.radius
#         print("area:",Area)
#     def perimeter(cir):
#         p=2*3.14*cir.radius
#         print("Perimeter:",p)
# obj=circle()
# obj.area()
# obj.perimeter()



# (0°C × 9/5) + 32 = 32°F
# (32°F − 32) × 5/9 = 0°C


class temp():
    def __init__(con):
        con.cel=int(input("enter temperature in celcius:"))
        con.far=int(input("enter temperature in farenheit:"))
    def confar(con):
        farenheit=con.cel*9/5+32
        print(farenheit)
    def concel(con):
        celcius=(con.far-32)*5/9
        print(celcius)
obj=temp()
obj.confar()
obj.concel()  
     


