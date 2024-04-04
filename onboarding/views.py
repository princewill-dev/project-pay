from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from .models import User, EmailVerification
from .utils import generate_otp
from django.core.mail import send_mail
from django.conf import settings

def homepage(request):
    return render(request, 'home/index.html')

def email_verification_view(request):
    return render(request, 'home/verify.html')

def plan_view(request):
    return render(request, 'home/pricing-plan.html')


# def signup_view(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('verify-email')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'home/signup.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            email = form.cleaned_data.get('email')
            otp = generate_otp()
            EmailVerification.objects.create(user=user, email=email, otp=otp)
            send_mail(
                'Email Verification',
                f'Your OTP is: {otp}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            # Redirect to a success page or the email verification page
            return redirect('email_verification')
    else:
        form = CustomUserCreationForm()
    return render(request, 'home/signup.html', {'form': form})


def email_verification_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = request.POST.get('otp')
        try:
            verification = EmailVerification.objects.get(email=email, otp=otp)
            user = verification.user
            user.is_active = True
            user.save()
            verification.delete()
            # Authenticate and login the user
            user_auth = authenticate(request, username=user.email, password=user.password)
            if user_auth is not None:
                login(request, user_auth)
            return redirect('home')
        except EmailVerification.DoesNotExist:
            return render(request, 'home/verify.html', {'error': 'Invalid email or OTP'})
    return render(request, 'home/verify.html')


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('email_verification') #change to dashboard
    else:
        form = CustomAuthenticationForm()
    return render(request, 'home/login.html', {'form': form})




def logout_view(request):
    logout(request)
    return redirect('home/index.html')

@login_required
def home_view(request):
    return render(request, 'home/index.html')