a=str(input("enter a string:"))
b="aeiouAEIOU"
i=0
count=0
for i in a:
    if i in b:
        count+=1
print("number of vowels:",count)