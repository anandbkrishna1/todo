from django.shortcuts import render

from app.models import*
from app.form import*

def home(request):
    return render(request,'base.html')


def upload(request):
    form=bookform()
    if(request.method=="POST"):
        form=bookform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return home(request)
    return render(request,'add.html',{'form':form})

def booklist(request):
    b=Book.objects.all()
    return render(request,'list.html',{'b':b})
def edit(request,p):
    m=Book.objects.get(pk=p)
    form=bookform(instance=m)
    if request.method=="POST":
        form=bookform(request.POST,request.FILES,instance=m)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request,'edit.html',{'form':form})


# Create your views here.
