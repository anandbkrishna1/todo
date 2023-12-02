def python():
    a="python"
    b=""
    for i in range(len(a)):
        if a[i]=="t" or a[i]=="h":
            a.format(i)
        else:
            b=b+a[i]
    for j in range(len(b)):
        print(b[j],end=".")       
python()
       

