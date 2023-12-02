# import re
# email=input("enter email:")
# if len(email)>=10:
#     x=re.match(r"[a-z 0-9]+[@]+[a-z]{5}[.]+[com,in]{2,3}",email)
#     if x:
#         print("valid")
#     else:
#         print("invalid")
# else:
#     print("not enough character")
    
    
    
import re
date=input("enter date:")

x=re.search("^(0[1-9]|[12]\d|3[01])-(0[1-9]|1[012])-([1-9]\d\d\d)$",date)
if x:
    print("valid")
else:
    print("invalid")

