from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# password for test user is Harry$1

# Create your views here.

def index(request):

    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)


        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
    # A backend authenticated the credentials
            return redirect("/")
        else:
    # No backend authenticated the credentials
            return render(request, 'login.html')


    return render(request, 'login.html')


def logoutUser(request):
     logout(request)
     return redirect("/login")
