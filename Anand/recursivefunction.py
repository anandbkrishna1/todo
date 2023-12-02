# def fact(n):
#     if n==1:
#         f=1
#     else:
#         f=n*fact(n-1)
#     return(f)
# num=int(input("enter number:"))
# result=fact(num)
# print("factotal is:",result)


# def num(n):
#     if n>=0:
#         a=n
#         print(a)
#         n=num(n-1)
#     return(a)
# b=int(input("enter number:"))
# r=num(b)
# print(r)

from functools import reduce

n=int(input("enter number:"))
fact=reduce(lambda a,b : a*b,range(1,n+1))
print(fact)