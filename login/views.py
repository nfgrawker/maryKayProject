from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homeLogin(request):
    context={
    }
    print(request)
    return render(request, "login/testLogin.html", context)

def forgotPassword(request):
    return HttpResponse("ForgotPasswordPage")

def registerAccount(request):
    context={
    }
    print(request)
    return render(request, "login/register.html", context)