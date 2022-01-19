from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'accounts/login.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def role(request):
    return render(request, 'accounts/role.html')

def user(request):
    return render(request, 'accounts/user.html')

def project(request):
    return render(request, 'accounts/project.html')

def ticket(request):
    return render(request, 'accounts/ticket.html')

def profile(request):
    return render(request, 'accounts/profile.html')
