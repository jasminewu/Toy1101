#-*-coding:utf8-*-

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .form import AddForm



def index(request):
    return HttpResponse("welcome django 1.8 version")

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a)+int(b)
    return HttpResponse(str(c))

def index2(request):
    return render(request,'home.html')

def old_add2_redirect(request):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )

def home(request):
    string = "home be called"
    paperList = ['一章','一章','yizhang',"erzhang"]
    paperdic = {'one1':'onePaper'}
    List = [x for x in range(100)]
    return render(request, 'home.html', {'string':string, 'list':paperList, 'paperdic':paperdic, 'List':List})

def form(request):
    return render(request,'index.html')

def add(request):
    a = requst.GET['a']
    b = requst.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))
def form2(request):
    if request.method == 'POST':#当提交表单时
        form = AddForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:#当正常访问时
        form = AddForm()
    return render(request, 'index2.html', {'form':form})
