# a=str(input("enter string:"))
# print(a)
# b=str
# b=a[::-1]
# print(b)
# if b==a:
#     print("string is palindrome")
# else:
#     print("not palindrome")
    
    
    
a=str(input("enter string:"))
words=a.split()
result=""
for w in words:
    if w==w[::-1]:
        for i in range(len(w)):
            b=len(w)*"@"
        result=result+b
    else:
        result=result+w
    result=result+" "
print(result)    