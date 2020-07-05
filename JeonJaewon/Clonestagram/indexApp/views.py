from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.


def signup(request):
    if request.method == "POST":
        if request.POST["username"] != "" and request.POST["password"] != "":
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password"])
            auth.login(request, user)
            return redirect('main')
    else:
        return render(request, 'signup.html')


def main(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            # return redirect('signup')
            return render(request, 'main.html', {'error': '아이디나 패스워드 오류입니다'})
    else:
        return render(request, 'main.html')


def home(request):
    return render(request, 'home.html')
