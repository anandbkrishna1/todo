class Restaurant():
    def __init__(self):
        self.menu=['chicken biriyani','beef biriyani','veg biriyani','chicken friedrice','veg  friedrice','ghee rice']
        self.table=[]
    def menu_items(self):
        print("MENU")
        print("----")
        for i in self.menu:
            print(i)
        print("_______________")
    def add_item(self):
        item=str(input("Enter item to add:"))
        self.menu.append(item)
        print("Item successfully added,Thank you")
       
    def book_table(self):
        tab=int(input("Enter table number:"))
        if tab in self.table:
            print("Sorry the table is already occupied")
        else:
            self.table.append(tab)
            print("Booking successful,Thank you")
            
    def place_order(self):
        order=str(input("Enter item:"))
        if order in self.menu:
            print("Order placed,Thank you")
        else:
            print("Sorry,item not available")
obj=Restaurant() 
while True:
    a=int(input("Enter choice:"))
    if a==1:
        obj.menu_items()
    elif a==2:
        obj.add_item()
    elif a==3:
        obj.book_table()
    elif a==4:
        obj.place_order()
    elif a==5:
        print("Exit")
        break
    else:
        print("WRONG CHOICE")
        
        
        