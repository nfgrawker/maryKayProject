from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import logout


# Create your views here.


def homeLogin(request):
    if request.user.is_authenticated():
        return redirect("/inventoryHome")
    context = {}
    print(request)
    return render(request, "login/homeLogin.html", context)


def forgotPassword(request):
    return HttpResponse("ForgotPasswordPage")


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("/login")


def termsAndConditions(request):
    return HttpResponse("COMING SOON!")


def mainRedirect(request):
    return redirect("/login")


def registerAccount(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print("saved")
            print(form.cleaned_data)
            firstName = form.cleaned_data.get("first_name")
            lastName = form.cleaned_data.get("last_name")
            messages.success(request, f"Account created for {firstName} {lastName}!")
            return redirect("/login")
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()

    return render(request, "login/register.html", {"form": form})
