def string():
    st=""
    for i in strg:
        if i.isalpha():
            st=st+i
    return st
strg=input("enter string:")
print(string())

