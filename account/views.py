from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if "next" in request.GET:
                return redirect(request.GET["next"])
            return redirect("default")
        else:
            messages.success(request, "Incorrect credentials, please try again.")
            return redirect("login")
    else:
        return render(request, "login.html", {})

def logout_view(request):
    logout(request)
    return redirect("default")