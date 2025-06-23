from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages


def home(request):
    return render(request, 'Accounts/home.html')

def register_view(request):
    # Que ingrese sin tener que poner la direccion que sea redirigido
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    form = RegisterForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = User.objects.create_user(username, email, password)
        if user:
            login(request, user)
            return redirect('dashboard')
    
    return render(request, 'Accounts/register.html',{
        'form': form
    })  
def login_view(request):
    # Que ingrese sin tener que poner la direccion que sea redirigido
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # base de datos 1 y variables 2
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)            
            return redirect('dashboard') #path('',views.index, name='index'), en urls.py
        else:
            messages.error(request, 'Usuarios o Contraseña no validos')
        
    return render(request,"Accounts/login.html", {
        
    })

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    return render(request, 'Accounts/dashboard.html')