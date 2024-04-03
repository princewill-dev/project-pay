from django.shortcuts import render

def homepage(request):
    return render(request, 'home/index.html')

def signup(request):
    return render(request, 'home/signup.html')
