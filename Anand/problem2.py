m=int(input("enter mark of maths:"))
p=int(input("enter mark of physics:"))
c=int(input("enter mark of chemistry:"))
t=m+p
print("total of chemistry and physics:",t)
if m>=55 and c>=50 and t>=140:
    print("passed")
else:
    print("failed")