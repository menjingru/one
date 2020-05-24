from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request,'login1.html')

def dologin(request):
    username = request.GET['username']
    pwd = request.GET['pwd']
    if username=='admin'and pwd=='1234':
        request.session['username']=username
        request.session.set_expiry(600)
        sessionID = request.session.session_key
        return render(request,'home.html',{"sessionID":sessionID})
    else:
        return HttpResponse('fail')
        # return render(request,'home.html')

def home(request):
    return render(request,'home.html')

def logout(request):
    del request.session['username']
    return render(request,'home.html')