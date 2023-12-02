from django.shortcuts import render
from django.http import HttpResponse
from app1.models import*
from app1.form import*
def home(request):
    d=student.objects.all()
    return render(request,'home.html',{'t':d})

def form1(request):
    form=studentform()
    if (request.method=='POST'):
        form=studentform(request.POST)
        if (form.is_valid()):
            form.save()
            return home(request)
    return render(request,'form1.html',{'form':form})

def form2(request):
    if (request.method=='POST'):
        form=studentform(request.POST)
        if (form.is_valid()):
            form.save()
            return home(request)
    return render(request,'form2.html',)



# def index(request):
#     return HttpResponse('hello welcome to this page')

# def index1(request):
#     return HttpResponse('start your project')

# def index2(request):
#     return HttpResponse('hello')




# Create your views here.
