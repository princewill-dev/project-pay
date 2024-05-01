from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from .models import User, PaymentLink
from .utils import generate_otp
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.contrib import messages
import random
import string
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
import datetime
from django.utils.dateparse import parse_datetime
from django.shortcuts import get_object_or_404
import qrcode
from django.http import HttpResponse
from io import BytesIO
import os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage





def generate_random_string(length=20):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def homepage(request):
    return render(request, 'home/index.html')

def email_verification_view(request):
    return render(request, 'home/verify.html')

def plan_view(request):
    return render(request, 'home/pricing-plan.html')

def choose_action_view(request):

    payment_links = PaymentLink.objects.filter(user=request.user)
    print(payment_links.count())  # This should print a non-zero value

    context = {
        'payment_links': payment_links
    }
    return render(request, 'home/choose-action.html', context)



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
            #     'Welcome to bitwade.com', 
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
                return redirect('choose_action')
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
        return redirect('choose_action')  # Redirect to 'choose_action' page
    
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
                        return redirect('choose_action')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'home/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('homepage')

@login_required
def home_view(request):
    return render(request, 'home/index.html')


def generate_qr_code(text):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add the text to the QR code
    qr.add_data(text)
    qr.make(fit=True)

    # Generate the QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Create a BytesIO object to store the image data
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer



def create_payment_view(request):
    return render(request, 'home/create-payment-link.html')



@login_required
def create_payment_save(request):    

    if request.method == 'POST':
        crypto = request.POST.get('crypto')
        tag_name = request.POST.get('tag_name')
        link_id = generate_random_string()
        wallet = request.POST.get('wallet')
        qr_code_image = generate_qr_code(wallet)
        filename = f'qr_code_{wallet}.png'
        path = default_storage.save(filename, ContentFile(qr_code_image.getvalue()))

        payment_link = PaymentLink.objects.create(
            user=request.user,
            link_id=link_id,
            wallet=wallet,
            crypto=crypto,
            tag_name=tag_name,
            qr_code_image=path,
        )

        payment_link.save()

    messages.success(request, 'Your payment link has been created.')
    return redirect('pay_links')
    

def get_pay_view(request, link_id):
    instance = get_object_or_404(PaymentLink, link_id=link_id)
    context = {
        'instance': instance,
    }

    return render(request, 'home/show_pay_link.html', context)



@login_required
def pay_links_view(request):
    # Get all the payment links created by the current user
    payment_links = PaymentLink.objects.filter(user=request.user)

    context = {
        'payment_links': payment_links
    }

    return render(request, 'home/pay_links.html', context)


@login_required
def payment_link_view(request, link_id):

    instance = get_object_or_404(PaymentLink, link_id=link_id)

    return render(request, 'home/payment_link.html', {'instance': instance})


