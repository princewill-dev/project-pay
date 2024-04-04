from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from .models import User
from .utils import generate_otp
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.contrib import messages
import random
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'home/index.html')

def email_verification_view(request):
    return render(request, 'home/verify.html')

def plan_view(request):
    return render(request, 'home/pricing-plan.html')

def generate_otp():
    return ''.join(random.choice('0123456789') for _ in range(6))

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            otp_code = generate_otp()
            user.otp_code = otp_code
            user.otp_created_at = timezone.now()
            user.save()

            login(request, user)

            # send_mail(
            #     'Welcome to Digit-Pay', 
            #     f'Here is your email verification code: {otp_code}',
            #     'api@princewilldev.com',
            #     [user.email],
            #     fail_silently=False
            # )

            return redirect('email_verification')
    else:
        form = CustomUserCreationForm()
    return render(request, 'home/signup.html', {'form': form})

@login_required
def email_verification_view(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        user = request.user
        if user.otp_code == otp and user.otp_created_at >= timezone.now() - timezone.timedelta(minutes=5):
            user.is_active = True
            user.email_verification = 'verified'
            user.otp_code = None
            user.save()
            return redirect('plans')
        else:
            messages.error(request, 'Invalid OTP code. Please try again.')
    return render(request, 'home/verify.html')


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            otp = form.cleaned_data['otp']
            user = authenticate(request, username=email, password=password, otp=otp)
            if user is not None:
                login(request, user)
                return redirect('plans')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'home/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('homepage')

@login_required
def home_view(request):
    return render(request, 'home/index.html')


# def email_verification_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         otp = request.POST.get('otp')
#         try:
#             verification = EmailVerification.objects.get(email=email, otp=otp)
#             user = verification.user
#             user.is_active = True
#             user.save()
#             verification.delete()
#             # Authenticate and login the user
#             user_auth = authenticate(request, username=user.email, password=user.password)
#             if user_auth is not None:
#                 login(request, user_auth)
#             return redirect('home')
#         except EmailVerification.DoesNotExist:
#             return render(request, 'home/verify.html', {'error': 'Invalid email or OTP'})
#     return render(request, 'home/verify.html')


