from django.shortcuts import render
from django.http import HttpResponse
from login.forms import loginForm
# Create your views here.
# def login(request):
#     return render(request,'login.html')

# def dologin(request):
#     name = request.GET['username']
#     pwd = request.GET['pwd']
#     age = request.GET['age']
#     result = name + pwd +age
#     return HttpResponse(result)

def login(request):
    #这是post方式
    if request.method == 'POST':
        form = loginForm(request.POST)
        #如果合法
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            result = name + "   " + str(age)
            return HttpResponse(result)
    #这是get方式
    else:
        form = loginForm()
    return render(request,'login.html',{'form':form})