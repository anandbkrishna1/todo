
list=[]
def createlist():
    a=int(input("enter limit:"))
    for i in range(a):
        ele=int(input("enter element:"))
        list.append(ele)
    print("list is:",list)
    
    
def addele():
    ele=int(input("enter element to insert:"))
    list.append(ele)
    print(list)


def replaceele():
    index=int(input("enter position of the element to be replaced:"))
    list.pop(index)
    ele=int(input("enter element to replace:"))
    list.insert(index,ele)
    print(list)

def removeele():
    index=int(input("enter position of the element to be removed:"))
    list.pop(index)
    print(list)
    
while True:
    n=int(input("enter choice:"))
    if n==1:
        createlist()
    elif n==2:
        addele()
    elif n==3:
        replaceele()
    elif n==4:
        removeele()
    elif n==5:
        print("Exit")
        break
    else:
        print("wrong choice")

    
               