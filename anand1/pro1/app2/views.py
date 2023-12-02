from django.shortcuts import render
from django.http import HttpResponse
from app2.models import*
from app2.form import*
def base(request):
    return render(request,'base.html')
def home(request):
    return render(request,'base.html')
def about(request):
    return render(request,'base.html')

def about(request):
    d=employee.objects.all()
    return render(request,'about.html',{'e':d})
def home(request):
    form=employeeform()
    if request.method=='POST':
        form=employeeform(request.POST)
        if form.is_valid():
            form.save
            return base(request)
    return render(request,'home.html',{'home':form})


# Create your views here.