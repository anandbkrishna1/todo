# i=1
# while(i<=5):
#     print("hello")
#     i+=1
# for i in range(1,10,2):
#     print(i)
# print(range(10))
a=str(input("enter a string:"))
i=0

# l=''
d={}
count=0
while i<len(a):
    s=a[i]
    if s in d:
        d[s]+=1
        # l+=a[i]

        # print(a[i],count)
        # d[a[i]]=count
    else:
        d[s]=1
       
        # count=1
        # l+=a[i]
      
        # d[a[i]]=count    
    i=i+1
print(d)