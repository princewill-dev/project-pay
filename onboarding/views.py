from django.shortcuts import render, redirect
from django.contrib.auth import login 
from .forms import SignupForm

def homepage(request):
    return render(request, 'home/index.html')

def signup(request):
    return render(request, 'home/signup.html')



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in directly
            return redirect('home')  # Redirect to a success page ('home' is an example)
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})