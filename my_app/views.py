from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = ToDoForm()
        todos = ToDo.objects.filter(user=user).order_by('priority')
        return render(request, 'home.html', context={'form': form, 'todos': todos})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Invalid credentials')

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        if password == confirmPassword:
            if User.objects.filter(username=username).exists():
                return HttpResponse('Username already exists')
            elif User.objects.filter(email=email).exists():
                return HttpResponse('Email already exists')
            else:
                user = User.objects.create_user(username, email, password)
                user.save()
                return redirect('login')
        else:
            return HttpResponse('Passwords do not match')

    return render(request, 'signup.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('index')


@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('home')
        else:
            return render(request, 'home.html', context={'form': form})


def delete_todo(request, id):
    ToDo.objects.get(pk=id).delete()
    return redirect('home')


def update_status(request,id,status):
    todo = ToDo.objects.get(pk=id)
    todo.status = status
    todo.save()
    return redirect('home')