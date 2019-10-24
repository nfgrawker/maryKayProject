from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homeLogin(request):
    context={
    }
    print(request)
    return render(request, "login/homeLogin.html", context)

def forgotPassword(request):
    return HttpResponse("ForgotPasswordPage")
def termsAndConditions(request):
    return HttpResponse("COMING SOON!")
def registerAccount(request):
    if request.method == "POST":
        print(request.post)
    context={
    }
    print(request)
    return render(request, "login/register.html", context)
