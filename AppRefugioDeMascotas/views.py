from contextlib import redirect_stderr
from email import message
import django
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse
from requests import request
# Create your views here.


def home(request):
    return render(request, 'index.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST['userTextbox']
        password = request.POST['passwordTextbox']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.success(request, "Bienvenido")
            return redirect('Inicio')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, "Usuario o contraseña invalidos")  
            return redirect('login')
            
    else:
        return render(request, 'login.html')
    
def logoutUser(request):
    logout(request)
    messages.success(request, "Adiooooos")
    return redirect('Inicio')

def registerUser(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "registrado")
            login(request,user)
            return redirect('Inicio')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form':form,})
