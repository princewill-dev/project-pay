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
from django.contrib.auth import get_user_model
import datetime
from django.utils.dateparse import parse_datetime






def homepage(request):
    return render(request, 'home/index.html')

def email_verification_view(request):
    return render(request, 'home/verify.html')

def plan_view(request):
    return render(request, 'home/pricing-plan.html')

def generate_otp():
    return ''.join(random.choice('0123456789') for _ in range(6))

def signup_view(request):
    if request.user.is_authenticated:  # Check if the user is already authenticated
        return redirect('plans')  # Redirect to 'plans' page
    
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
        if user.otp_code == otp:
            if user.otp_created_at >= timezone.now() - timezone.timedelta(minutes=10):
                user.is_active = True
                user.email_verification = 'verified'
                user.otp_code = None
                user.otp_verified_at = timezone.now()
                user.save()
                return redirect('plans')
            else:
                messages.error(request, 'OTP expired. Please request for another one.')
        else:
            messages.error(request, 'Invalid OTP code. Please try again.')
    return render(request, 'home/verify.html')


@login_required
def generate_otp_view(request):
    last_access = request.session.get('last_access', None)
    if last_access:
        last_access = parse_datetime(last_access)  # Convert the string back to a datetime object
        time_since_last_access = timezone.now() - last_access
        if time_since_last_access.total_seconds() < 600:  # 600 seconds = 10 minutes
            messages.error(request, 'You can only generate a new OTP once every 10 minutes.')
            return redirect('email_verification')
    user = request.user
    user.otp_code = ''.join(random.choice('0123456789') for _ in range(6))  # Generate a new 6-digit OTP
    user.otp_created_at = timezone.now()  # Update the OTP creation time
    user.save()
    messages.success(request, 'New OTP has been generated.')  # Add a success message
    request.session['last_access'] = str(timezone.now().isoformat())  # Convert the datetime object to a string before storing it in the session
    return redirect('email_verification')  # Redirect back to the email verification page


def login_view(request):
    if request.user.is_authenticated:  # Check if the user is already authenticated
        return redirect('plans')  # Redirect to 'plans' page
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = get_user_model().objects.filter(email=email).first()  # Get the user instance associated with the email
            if user is not None:
                user = authenticate(request, username=email, password=password)
                if user is not None:
                    login(request, user)  # Log the user in first
                    if user.email_verification == 'unverified':
                        return redirect('email_verification')
                    else:
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


