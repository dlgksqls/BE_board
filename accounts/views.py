from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from .forms import SignUpform
from .models import User


# Create your views here.


def signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password"],  # 이게 왜 되노?
                email=request.POST["email"],
            )
            return redirect("board:home")
        return render(request, "accounts/signup.html")
    return render(request, "accounts/signup.html")


def login_view(request):
    if request.method == "GET":
        return render(request, "accounts/login.html")
    else:
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("board:home")
        else:
            return render(
                request,
                "accounts/login.html",
                {"error": "Username or password is incorrect"},
            )


def logout_view(request):
    auth.logout(request)
    return redirect("accounts:login")
