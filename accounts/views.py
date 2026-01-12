from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib import messages
from django.contrib.auth import login

def index(request):
    return render(request, 'accounts/index.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account created for {user.username}')
            return redirect('accounts:login')
    form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'You are logged in')
            return redirect('accounts:index')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('accounts:login')

    form = CustomLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

