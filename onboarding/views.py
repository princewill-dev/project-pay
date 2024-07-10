from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from .models import User, PaymentLink, Payment, Invoice, Wallet, Token
from .utils import generate_otp
from django.core.mail import send_mail
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
import json
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import time
from .forms import PaymentLinkForm
from decimal import Decimal, ROUND_DOWN
import math
from django.db.models import Sum
from django.views.decorators.http import require_http_methods
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.urls import reverse
from django.http import HttpRequest
import hashlib
from qrcode.image.svg import SvgImage
from django.core.files import File
import logging
from django.db import IntegrityError
from django.http import Http404
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives




# def generate_random_string():
#     random_string = ''.join(random.choice(string.digits) for _ in range(12))
#     return random_string

def generate_random_string(length=15):
    characters = string.ascii_lowercase + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def homepage(request):
    # return render(request, 'home/index.html')
    return render(request, 'landing/index.html')


def about_page_view(request):
    return render(request, 'landing/about.html')


def support_page_view(request):
    return render(request, 'landing/support.html')


def success_page_view(request):
    return render(request, 'home/temp_success_page.html')


def email_verification_view(request):
    return render(request, 'home/verify.html')


def plans_view(request):
    return render(request, 'home/pricing_plan.html')


def dashboard_view(request):
    payment_links = PaymentLink.objects.filter(user=request.user)
    transactions = Payment.objects.filter(user=request.user)
    successful_transactions = Payment.objects.filter(user=request.user, status='successful')
    total_successful_transactions = successful_transactions.aggregate(Sum('amount'))['amount__sum'] or 0
    invoices = Invoice.objects.filter(user=request.user)  # Fetch the invoices
    account_id = request.user.account_id
    account_email = request.user.email

    # Calculate total successful transactions for each PaymentLink
    for link in payment_links:
        link.total_successful_transactions = Payment.objects.filter(payment_link=link, status='successful').aggregate(Sum('amount'))['amount__sum'] or 0

    context = {
        'transactions': transactions,
        'payment_links': payment_links,
        'invoices': invoices,  # Pass the invoices to the context
        'account_id': account_id,
        'account_email': account_email,
        'total_successful_transactions': total_successful_transactions,
    }
    return render(request, 'home/dashboard.html', context)


def generate_otp():
    return ''.join(random.choice('0123456789') for _ in range(6))


def signup_view(request):
    if request.user.is_authenticated:  # Check if the user is already authenticated
        return redirect('dashboard')  # Redirect to 'plans' page
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save the user object yet
            otp_code = generate_otp()
            user.otp_code = otp_code
            user.otp_created_at = timezone.now()

            try:
                send_mail(
                    'Welcome to bixmerchant.com', 
                    f'Here is your email verification code: {otp_code}',
                    'support@bixmerchant.com',
                    [user.email],
                    fail_silently=False
                )
            except Exception as e:
                # Handle the exception e.g. show an error message to the user
                # return render(request, 'home/signup.html', {'form': form, 'error': 'Could not send the OTP email.'})
                messages.success(request, 'Could not send the OTP email.')
                return redirect('signup_page')

            user.save()  # Now save the user object

            login(request, user)

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
                return redirect('create_payment_link')
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
        return redirect('dashboard')  # Redirect to 'dashboard' page
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
                        return redirect('dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'home/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login_page')


def password_reset_request(request):
    if request.method == "POST":
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            
            current_site = get_current_site(request)
            mail_subject = 'Password Reset Requested'

            message = f"""
            Hi,

            You have requested a password reset. Please go to the following page and choose a new password:

            http://{current_site.domain}/reset/{uid}/{token}

            If you didn't request this, please ignore this email.

            """
            send_mail(mail_subject, message, 'support@bixmerchant.com', [user.email])
            messages.success(request, 'Please check your email for the password reset link.')
            return render(request, 'home/reset_password.html')
        else:
            messages.error(request, 'Invalid email address.')
            return render(request, 'home/reset_password.html')
    return render(request, 'home/reset_password.html')


def password_reset_confirm_view(request, uidb64, token):

    User = get_user_model()
    
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password reset was successful.')
                return redirect('login_page')
            else:
                messages.error(request, 'Passwords do not match.')
        return render(request, 'home/reset_pssword_new.html')
    else:
        messages.error(request, 'The reset password link is invalid.')
        return redirect('password_reset')


@login_required
def home_view(request):
    return render(request, 'home/index.html')


def generate_qr_code(text):
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError('The text argument must be a string')

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
    img = qr.make_image(fill_color="black", back_color="white", image_factory=SvgImage)
    # Generate a filename based on the text
    filename = hashlib.md5(text.encode()).hexdigest() + ".svg"
    # Save the image to a file in the mediafiles directory
    img_path = os.path.join(settings.MEDIA_ROOT, 'qr_codes/', filename)
    img.save(img_path)

    return filename


@login_required
def create_payment_link_view(request):
    return render(request, 'home/create_payment_link.html')


@login_required
def select_coins_view(request):
    tokens = Token.objects.filter(is_active=True)
    return render(request, 'home/select_coins.html', {'tokens': tokens})


@login_required
def edit_payment_wallets_view(request, link_id):
    tokens = Token.objects.filter(is_active=True)

    # Get the wallets associated with the payment_link
    wallets = Wallet.objects.filter(wallet_id=link_id)

    payment_link = PaymentLink.objects.get(link_id=link_id)

    context = {
        'payment_link': payment_link,
        'tokens': tokens,
        'wallets': wallets,
    }

    return render(request, 'home/edit_store_wallet.html', context)


@login_required
def update_payment_wallets_view(request, link_id):

    if request.method == 'POST':

        # Get the PaymentLink instance corresponding to the link_id
        payment_link = PaymentLink.objects.get(link_id=link_id)

        # Delete any existing Wallet instances associated with this PaymentLink
        Wallet.objects.filter(wallet_id=payment_link).delete()

        # Create Wallet instances for each selected cryptocurrency
        for token in Token.objects.all():
            wallet_address = request.POST.get(f'{token.token_tag}_wallet')
            if wallet_address:  # Only save if a wallet address is provided

                Wallet.objects.create(
                    user=request.user,
                    wallet_id=payment_link,
                    crypto=token.token_tag,
                    address=wallet_address,
                    # qr_code_image=qr_code_image,
                )

        messages.success(request, 'Your store wallets has been updated.')
        return redirect('show_payment_link', link_id=link_id)

    return redirect('create_payment_link_form')


@login_required
def save_payment_link_view(request):    
    if request.method == 'POST':
        content_file = None  # Initialize content_file

        if 'image' in request.FILES:
            image = request.FILES['image']
            # Check if the file is a .png or .webp and its size is less than or equal to 5MB
            if not (
                image.name.endswith('.png')
                or
                image.name.endswith('.webp')
                or
                image.name.endswith('.jpg')
                or
                image.name.endswith('.jpeg')
                ) or image.size > 5 * 1024 * 1024:
                messages.error(request, 'Invalid image. Please upload a .png, .webp, .jpg, or .jpeg image that is less than 5MB.')
                return redirect('create_payment_link_form')

            content_file = image  # Assign the image directly to content_file

        tag_name = request.POST.get('tag_name')
        link_url = request.POST.get('link_url')
        # callback_url = request.POST.get('callback_url')
        link_description = request.POST.get('link_description')
        link_id = generate_random_string()

        # Create a PaymentLink instance
        payment_link = PaymentLink.objects.create(
            user=request.user,
            link_id=link_id,
            tag_name=tag_name,
            link_logo=content_file,
            link_url=link_url,
            # callback_url=callback_url,
            link_description=link_description,
        )

        # Store the link_id in the session
        request.session['link_id'] = link_id

        return redirect('select_coins')

    return redirect('create_payment_link_form')


@login_required
def save_selected_coins_view(request):    
    if request.method == 'POST':

        # Retrieve the link_id from the session
        link_id = request.session.get('link_id')

        # Get the PaymentLink instance corresponding to the link_id
        payment_link = PaymentLink.objects.get(link_id=link_id)

        # Create Wallet instances for each selected cryptocurrency
        for token in Token.objects.all():
            wallet_address = request.POST.get(f'{token.token_tag}_wallet')
            if wallet_address:  # Only save if a wallet address is provided

                qr_code_image = generate_qr_code(wallet_address)

                # filename = f'{wallet_address}_{payment_link.link_id}.png'

                # qr_code_image_file = ContentFile(qr_code_image.getvalue(), name=filename)

                Wallet.objects.create(
                    user=request.user,
                    wallet_id=payment_link,
                    crypto=token.token_tag,
                    address=wallet_address,
                    qr_code_image=qr_code_image,
                )

        messages.success(request, 'Your store link has been created.')
        return redirect('show_payment_link', link_id=link_id)

    return redirect('create_payment_link_form')


# Get all the payment links created by the current user
@login_required
def show_all_payment_links_view(request):
    payment_links = PaymentLink.objects.filter(user=request.user)
    transactions = Payment.objects.filter(user=request.user)
    successful_transactions = Payment.objects.filter(user=request.user, status='successful')
    total_successful_transactions = successful_transactions.aggregate(Sum('amount'))['amount__sum'] or 0
    invoices = Invoice.objects.filter(user=request.user)  # Fetch the invoices
    account_id = request.user.account_id
    account_email = request.user.email

    # Calculate total successful transactions for each PaymentLink
    for link in payment_links:
        link.total_successful_transactions = Payment.objects.filter(payment_link=link, status='successful').aggregate(Sum('amount'))['amount__sum'] or 0

    context = {
        'transactions': transactions,
        'payment_links': payment_links,
        'invoices': invoices,  # Pass the invoices to the context
        'account_id': account_id,
        'account_email': account_email,
        'total_successful_transactions': total_successful_transactions,
    }
    return render(request, 'home/payment_links.html', context)

@login_required
def edit_payment_link_view(request, link_id):

    payment_link = get_object_or_404(PaymentLink, link_id=link_id, user=request.user)

    # Get the wallets associated with the payment_link
    wallets = Wallet.objects.filter(wallet_id=payment_link)

    context = {
        'payment_link': payment_link,
        'wallets': wallets,
    }

    return render(request, 'home/edit_payment_link.html', context)


@login_required
def update_payment_link_view(request, link_id):
    if request.method == 'POST':

        payment_link = get_object_or_404(PaymentLink, link_id=link_id, user=request.user)

        content_file = None  # Initialize content_file

        if 'image' in request.FILES:
            image = request.FILES['image']
            # Check if the file is a .png or .webp and its size is less than or equal to 5MB
            if not (
                image.name.endswith('.png')
                or
                image.name.endswith('.webp')
                or
                image.name.endswith('.jpg')
                or
                image.name.endswith('.jpeg')
                ) or image.size > 5 * 1024 * 1024:
                messages.error(request, 'Invalid image. Please upload a .png, .webp, .jpg, or .jpeg image that is less than 5MB.')
                return redirect('create_payment_link_form')

            content_file = image  # Assign the image directly to content_file

        # Update the PaymentLink instance
        payment_link.tag_name = request.POST.get('tag_name')
        payment_link.link_url = request.POST.get('link_url')
        # payment_link.callback_url = request.POST.get('callback_url')
        if content_file is not None:  # Only assign content_file to link_logo if content_file is not None
            payment_link.link_logo = content_file
        payment_link.link_description = request.POST.get('link_description')
        payment_link.save()

        messages.success(request, 'store info updated successfully.')
        return redirect('show_payment_link', link_id=link_id)

    # If the request method is not POST, redirect to the edit page
    return redirect('edit_payment_link', link_id=link_id)


@login_required
def edit_payment_link_wallet_view(request, link_id):

    payment_link = get_object_or_404(PaymentLink, link_id=link_id, user=request.user)

    if request.method == 'POST':

        tag_name = request.POST.get('tag_name')
        link_url = request.POST.get('link_url')
        store_description = request.POST.get('store_description')
        link_id = generate_random_string()

        # Create a PaymentLink instance
        payment_link = PaymentLink.objects.create(
            user=request.user,
            link_id=link_id,
            tag_name=tag_name,
            link_url=link_url,
            store_description=store_description,
        )

        messages.success(request, 'Your store information has been updated.')
        return redirect('select_coins')

    return render(request, 'home/edit_payment_link.html', {'payment_link': payment_link})


# shows all Payment made to the user
@login_required
def show_transactions_view(request):
    transactions = Payment.objects.filter(user=request.user)
    context = {
        'transactions': transactions,
    }
    return render(request, 'home/transactions_table.html', context)


def show_payment_link_view(request, link_id):
    payment_link = get_object_or_404(PaymentLink, link_id=link_id)
    transactions = Payment.objects.filter(payment_link=payment_link)  # Filter transactions by payment_link
    successful_payments = Payment.objects.filter(payment_link=payment_link, status='successful')
    total_successful_payments = successful_payments.aggregate(Sum('amount'))['amount__sum'] or 0
    context = {
        'payment_link': payment_link,
        'total_successful_payments': total_successful_payments,
        'transactions': transactions,  # Add transactions to the context
    }
    return render(request, 'home/show_payment_link.html', context)


@login_required
def delete_payment_link_view(request, link_id):
    payment_link = get_object_or_404(PaymentLink, link_id=link_id, user=request.user)
    payment_link.delete()
    messages.success(request, 'Payment link deleted successfully.')
    return redirect('show_all_payment_links')


@csrf_exempt
def generate_transaction_view(request, link_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            payment_link = PaymentLink.objects.get(link_id=link_id)
        except PaymentLink.DoesNotExist:
            return JsonResponse({"error": "Invalid payment link ID"}, status=400)

        try:
            payment = Payment.objects.create(
                user=payment_link.user,
                payment_link=payment_link,
                transaction_id=generate_random_string(),
                amount=data['amount'],
                success_url=data['success_url'],
            )
            return JsonResponse({

                "message": "payment generated successfully",
                "transaction_id": payment.transaction_id,
                "transactin_url": f"{request.get_host()}/invoice/{payment.transaction_id}",

            }, status=201)
        
        except IntegrityError as e:
            return JsonResponse({"error": f"Failed to create payment: {str(e)}"}, status=500)
    else:
        return HttpResponse(status=405)
    


#API requests starts here

@csrf_exempt
@require_http_methods(['POST'])
def transaction_checkout_view(request):

    CUSTOM_API_KEY_HEADER = 'BIXMERCHANT_API_KEY'  # Already converted to Django's header format

    api_key = request.META.get(f'HTTP_{CUSTOM_API_KEY_HEADER}')
    if not api_key:
        return JsonResponse({"error": "No API key provided in the headers"}, status=400)

    try:
        payment_link = PaymentLink.objects.get(api_key=api_key)
    except PaymentLink.DoesNotExist:
        return JsonResponse({"error": "Invalid API key"}, status=403)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    required_fields = ['amount', 'email', 'item']
    if not all(field in data for field in required_fields):
        return JsonResponse({"error": "Missing required fields"}, status=400)

    try:
        payment = Payment.objects.create(
            user=payment_link.user,
            payment_link=payment_link,
            transaction_id=generate_random_string(),
            amount=data['amount'],
            email=data['email'],
            item=data['item'],
            # success_url=payment_link.callback_url
            success_url=data['success_url'],
        )
        return JsonResponse({
            "status": payment.status,
            "amount": data['amount'],
            "message": "Payment generated successfully",
            "created_at": payment.created_at,
            "transaction_id": payment.transaction_id,
            "transaction_url": f"{request.get_host()}/invoice/{payment.transaction_id}",
        }, status=201)
    except IntegrityError as e:
        logging.error(f"IntegrityError: {e}")
        return JsonResponse({"error": f"Failed to create payment: {str(e)}"}, status=500)


@csrf_exempt
@require_http_methods(['POST'])
def web_checkout_view(request):

    data = request.POST
    required_fields = ['amount', 'email', 'item', 'success_url', 'access_key']
    if not all(field in data for field in required_fields):
        messages.error(request, 'Missing required fields')
        return render(request, 'home/invalid_payment.html')

    try:
        payment_link = PaymentLink.objects.get(access_key=data['access_key'])
    except PaymentLink.DoesNotExist:
        messages.error(request, 'Invalid access key')
        return render(request, 'home/invalid_payment.html', {"error": "Invalid access key"})

    try:
        payment = Payment.objects.create(
            user=payment_link.user,
            payment_link=payment_link,
            transaction_id=generate_random_string(),
            amount=data['amount'],
            email=data['email'],
            item=data['item'],
            success_url=data['success_url'],
        )
        return redirect(f"/invoice/{payment.transaction_id}")
    except IntegrityError as e:
        logging.error(f"IntegrityError: {e}")
        messages.error(request, f"Failed to create payment: {str(e)}")
        return render(request, 'home/invalid_payment.html')
    

@csrf_exempt
@require_http_methods(['POST'])
def transaction_validate_json_view(request):
    CUSTOM_API_KEY_HEADER = 'BIXMERCHANT_API_KEY'  # Already converted to Django's header format

    api_key = request.META.get(f'HTTP_{CUSTOM_API_KEY_HEADER}')
    if not api_key:
        return JsonResponse({"error": "No API key provided in the headers"}, status=400)

    try:
        payment_link = PaymentLink.objects.get(api_key=api_key)
    except PaymentLink.DoesNotExist:
        return JsonResponse({"error": "Invalid API key"}, status=403)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    if 'transaction_id' not in data:
        return JsonResponse({"error": "Missing required field: transaction_id"}, status=400)

    transaction_id = data['transaction_id']

    try:
        payment = Payment.objects.get(transaction_id=transaction_id, payment_link=payment_link)
    except Payment.DoesNotExist:
        return JsonResponse({"error": "Transaction not found"}, status=404)

    message = "Transaction validated successfully"
    if payment.status == 'pending':
        message = "Transaction pending"

    return JsonResponse({
        "status": payment.status,
        "message": message,
        "transaction_id": payment.transaction_id,
        "amount": payment.amount,
        "item": payment.item,
        "customer_email": payment.email,
        "created_at": payment.created_at,
    }, status=200)


@csrf_exempt
@require_http_methods(['GET'])
def transaction_validate_url_view(request, tx_id):
    CUSTOM_API_KEY_HEADER = 'BIXMERCHANT_API_KEY'  # Already converted to Django's header format

    api_key = request.META.get(f'HTTP_{CUSTOM_API_KEY_HEADER}')
    if not api_key:
        return JsonResponse({"error": "No API key provided in the headers"}, status=400)

    try:
        payment_link = PaymentLink.objects.get(api_key=api_key)
    except PaymentLink.DoesNotExist:
        return JsonResponse({"error": "Invalid API key"}, status=403)

    try:
        payment = Payment.objects.get(transaction_id=tx_id, payment_link=payment_link)
    except Payment.DoesNotExist:
        return JsonResponse({"error": "Transaction not found"}, status=404)

    message = "Transaction validated successfully"
    if payment.status == 'pending':
        message = "Transaction pending"

    return JsonResponse({
        "status": payment.status,
        "message": message,
        "transaction_id": payment.transaction_id,
        "amount": payment.amount,
        "item": payment.item,
        "customer_email": payment.email,
        "created_at": payment.created_at,
    }, status=200)


#API requests stops here
    

def get_wallet_info(payment_link, crypto):
    wallets = payment_link.wallet_set.filter(crypto=crypto)
    wallet_info = []
    for wallet in wallets:
        wallet_info.append({
            'wallet': wallet.address,
            'crypto': wallet.crypto,
            'qr_code_image': wallet.qr_code_image.url if wallet.qr_code_image else '',
        })
    return wallet_info


def convert_usd_to_trx(amount_in_usd):
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=tron&vs_currencies=usd')
    data = response.json()
    trx_per_usd = Decimal(1) / Decimal(data['tron']['usd']).quantize(Decimal('0.000001'), rounding=ROUND_DOWN)
    return (amount_in_usd * trx_per_usd).quantize(Decimal('0.000001'), rounding=ROUND_DOWN)


def random_amount_generator():
    amount = round(random.uniform(0.01, 0.50), 2)
    return amount

    
def save_crypto_selection_view(request, tx_id):

    invoice_id = get_object_or_404(Payment, transaction_id=tx_id)

    status_check_response = check_invoice_status(request, invoice_id)
    if status_check_response:
        return status_check_response

    if request.method == 'POST':
        
        selected_crypto = request.POST.get('selected_crypto')

        wallet = invoice_id.payment_link.wallet_set.filter(crypto=selected_crypto).first()

        targeted_address = wallet.address

        random_added_amount = random_amount_generator()
        print(random_added_amount)

        amount_in_usd = invoice_id.amount + Decimal(random_added_amount)

        amount_in_trx = convert_usd_to_trx(amount_in_usd)

        if selected_crypto == 'TRX':

            api_link = f'https://api.trongrid.io/v1/accounts/{targeted_address}/transactions/'

            converted_amt = amount_in_trx

        elif selected_crypto == 'TRC20':

            api_link = f'https://api.trongrid.io/v1/accounts/{targeted_address}/transactions/trc20?limit=100&contract_address=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t'

            converted_amt = amount_in_usd

        # Update the database where this transaction exists
        invoice_id.crypto_network = selected_crypto
        invoice_id.wallet_address = wallet.address
        invoice_id.converted_amount = converted_amt
        invoice_id.random_added_amount = random_added_amount
        invoice_id.api_url = api_link
        invoice_id.save()

        return redirect('confirm_email_for_receipt', tx_id=invoice_id.transaction_id)

    # Handle GET requests
    return redirect('select_transaction_crypto', tx_id=invoice_id.transaction_id)


def get_transaction_status(tx_id):

    try:

        invoice = Payment.objects.get(transaction_id=tx_id)
        
        transaction_details = {
            'user': invoice.user,
            'payment_link': invoice.payment_link.link_id,
            'transaction_id': invoice.transaction_id,
            'amount': invoice.amount,
            'converted_amount': invoice.converted_amount,
            'random_added_amount': invoice.random_added_amount,
            'item': invoice.item,
            'ip_address': invoice.ip_address,
            'user_agent': invoice.user_agent,
            'country': invoice.country,
            'email': invoice.email,
            'crypto_network': invoice.crypto_network,
            'wallet_address': invoice.wallet_address,
            'transaction_hash': invoice.transaction_hash,
            'api_url': invoice.api_url,
            'tag_name': invoice.business_name,
            'created_at': invoice.created_at,
            'is_paid': invoice.is_paid,
            'success_url': invoice.success_url,
            'status': invoice.status,
            'find_tx_counter': invoice.find_tx_counter,
            'completion_time': invoice.completion_time,
        }

        if invoice.status in ['successful', 'cancelled', 'expired', 'suspended']:
           
            return {
                'status': 'ok',
                'transaction_details': transaction_details
            }
        
    except Payment.DoesNotExist:
        return {
            'status': 'error',
            'action_page': 'home/error_page.html',
        }


def check_invoice_status(request, invoice_id):
    # Get the invoice
    invoice = get_object_or_404(Payment, transaction_id=invoice_id)

    transaction_details = {
        'transaction_id': invoice.transaction_id,
        'payment_link': invoice.payment_link.link_id,
        'amount': invoice.amount,
        'success_url': invoice.success_url,
        'created_at': invoice.created_at,
        'is_paid': invoice.is_paid,
        'status': invoice.status,
        'tag_name': invoice.payment_link.tag_name,
        'return_url': invoice.success_url,
        'transaction_hash': invoice.transaction_hash,
    }

    # Check if the invoice is already successful
    if invoice.status == 'successful':
        messages.success(request, 'This invoice has already been paid.')
        return render(request, 'home/temp_success_page.html', {'transaction_details': transaction_details})

    # Check if the invoice status is cancelled
    if invoice.status == 'cancelled':
        messages.error(request, 'This invoice has been cancelled.')
        return render(request, 'home/invalid_payment.html', {'transaction_details': transaction_details})

    # Check if the current time has exceeded the completion time
    if invoice.completion_time and timezone.now() > invoice.completion_time:
        invoice.status = 'expired'
        invoice.success_url = f'{invoice.payment_link}?transaction_id={invoice.transaction_id}&status=expired'
        invoice.save()
        messages.error(request, 'This invoice has expired. Please try again.')
        return render(request, 'home/invalid_payment.html', {'transaction_details': transaction_details})

    return None


def select_transaction_crypto_view(request, tx_id):

    try:
        
        # Get the Payment object with the given transaction ID
        invoice_id = Payment.objects.get(transaction_id=tx_id)

        status_check_response = check_invoice_status(request, invoice_id)
        if status_check_response:
            return status_check_response

        # Get the PaymentLink associated with the transaction
        payment_link = invoice_id.payment_link

        # Get the crypto and address connected to the transaction
        crypto_networks = Wallet.objects.filter(wallet_id=payment_link)
        if crypto_networks.exists():
            available_cryptos = list(crypto_networks.values_list('crypto', flat=True))
        else:
            # Handle the case when the wallet does not exist
            available_cryptos = "Unknown"

        # Get the user's IP address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip_address = x_forwarded_for.split(',')[0]
        else:
            ip_address = request.META.get('REMOTE_ADDR')

        # Get the user's user agent
        user_agent = request.META.get('HTTP_USER_AGENT')

        # Update the database where this transaction exists
        invoice_id.ip_address = ip_address
        invoice_id.user_agent = user_agent
        invoice_id.save()

        # Get the transaction details
        transaction_details = {
            'transaction_id': invoice_id.transaction_id,
            'payment_link': invoice_id.payment_link.link_id,
            'amount': invoice_id.amount,
            'success_url': invoice_id.success_url,
            'created_at': invoice_id.created_at,
            'is_paid': invoice_id.is_paid,
            'status': invoice_id.status,
            'tag_name': invoice_id.payment_link.tag_name,
        }

        context = {
            'transaction_details': transaction_details,
            'available_cryptos': available_cryptos,
        }

        return render(request, 'home/select_transaction_crypto.html', context)
    
    except Payment.DoesNotExist:
        # Render the error page if the Payment object does not exist
        messages.error(request, 'Transaction not found.')
        return render(request, 'home/invalid_payment.html')


def confirm_email_for_receipt_view(request, tx_id):

    try:
        # Get the Payment object with the given transaction ID
        invoice_id = Payment.objects.get(transaction_id=tx_id)

        status_check_response = check_invoice_status(request, invoice_id)
        if status_check_response:
            return status_check_response

        if invoice_id.status == 'successful':

            transaction_details = {
                'transaction_id': invoice_id.transaction_id,
                'payment_link': invoice_id.payment_link.link_id,
                'amount': invoice_id.amount,
                'email': invoice_id.email,
                'success_url': invoice_id.success_url,
                'created_at': invoice_id.created_at,
                'is_paid': invoice_id.is_paid,
                'status': invoice_id.status,
                'tag_name': invoice_id.payment_link.tag_name,
                'hash': invoice_id.transaction_hash,
                'link_logo': invoice_id.payment_link.link_logo
            }

            context = {
                'transaction_details' : transaction_details,
            }

            return render(request, 'home/temp_success_page.html', context)

        # Get the PaymentLink associated with the transaction
        payment_link = invoice_id.payment_link

        # Get the transaction details
        transaction_details = {
            'transaction_id': invoice_id.transaction_id,
            'payment_link': invoice_id.payment_link.link_id,
            'amount': invoice_id.amount,
            'email': invoice_id.email,
            'success_url': invoice_id.success_url,
            'created_at': invoice_id.created_at,
            'is_paid': invoice_id.is_paid,
            'status': invoice_id.status,
            'tag_name': invoice_id.payment_link.tag_name,
        }

        context = {
            'transaction_details': transaction_details
        }

        return render(request, 'home/verify_email_receipt.html', context)
    
    except Payment.DoesNotExist:
        messages.error(request, 'Transaction not found.')
        return render(request, 'home/invalid_payment.html')
    

def save_confirm_email_for_receipt_view(request, tx_id):

    invoice_id = get_object_or_404(Payment, transaction_id=tx_id)

    if request.method == 'POST':
        
        confirmed_email = request.POST.get('email')

        # Update the database where this transaction exists

        time_to_complete = timezone.now() + timezone.timedelta(minutes=10)
        invoice_id.completion_time = time_to_complete
        invoice_id.email = confirmed_email
        invoice_id.save()

        return redirect('make_payment_page', tx_id=invoice_id.transaction_id)

    # Handle GET requests
    return redirect('select_transaction_crypto', tx_id=invoice_id.transaction_id)


def make_payment_view(request, tx_id):
    try:
        invoice_id = Payment.objects.get(transaction_id=tx_id)

        status_check_response = check_invoice_status(request, invoice_id)
        if status_check_response:
            return status_check_response

        selected_crypto = invoice_id.crypto_network
        converted_amount = invoice_id.converted_amount
        targeted_address = invoice_id.wallet_address
        qr_result = targeted_address + "?amount=" + str(converted_amount)
        qr_code_image = generate_qr_code(qr_result)
        qr_code = qr_code_image

        created_at = invoice_id.created_at
        time_to_complete = invoice_id.completion_time

        # Calculate the difference in seconds
        time_difference = int((time_to_complete - timezone.now()).total_seconds())

        transaction_details = {
            'transaction_id': invoice_id.transaction_id,
            'payment_link': invoice_id.payment_link.link_id,
            'amount': invoice_id.amount,
            'converted_amount': invoice_id.converted_amount,
            'charges': invoice_id.random_added_amount,
            'success_url': invoice_id.success_url,
            'created_at': invoice_id.created_at,
            'is_paid': invoice_id.is_paid,
            'status': invoice_id.status,
            'tag_name': invoice_id.payment_link.tag_name,
            'wallet': targeted_address,
            'crypto_network': selected_crypto,
            'qr_code': qr_code,
            'completion_time': invoice_id.completion_time,
            'time_difference': time_difference,
        }

        context = {
            'transaction_details': transaction_details,
        }
        return render(request, 'home/make_payment.html', context)
    
    except Payment.DoesNotExist:
        # Render the error page if the Payment object does not exist
        messages.error(request, 'Transaction not found.')
        return render(request, 'home/invalid_payment.html')
    

def cancel_transaction_view(request, tx_id):
    transaction = get_object_or_404(Payment, transaction_id=tx_id)

    # Mark the transaction status as "cancelled"
    transaction.status = 'cancelled'
    # Update the success_url with query parameters indicating the transaction has been cancelled
    transaction.success_url = f'{transaction.success_url}?transaction_id={transaction.transaction_id}&status=cancelled'
    transaction.save()

    # Redirect to the success_url
    return redirect(transaction.success_url)
    

def send_email(invoice_tx, recipient, is_customer):

    recipient_email = recipient
    
    if is_customer:
        mail_subject = f'{invoice_tx.payment_link.tag_name} Receipts'
        message = f"""
            Payment processed successfully
            Amount: ${invoice_tx.amount}
            Invoice: {invoice_tx.transaction_id}
            Store: {invoice_tx.payment_link.tag_name}
        """
    else:
        mail_subject = f'New Order on {invoice_tx.payment_link.tag_name} [{invoice_tx.transaction_id}]'
        message = f"""
            You have a new purchase
            Amount: ${invoice_tx.amount} - {invoice_tx.converted_amount} {invoice_tx.crypto_network}
            Invoice: {invoice_tx.transaction_id}
            Item: {invoice_tx.item}
            Customer email: {recipient_email}
        """
    send_mail(mail_subject, message, 'support@bixmerchant.com', [recipient_email])


def blockchain_api_view(request, tx_id):
    try:
        invoice_tx = Payment.objects.get(transaction_id=tx_id)
    except Payment.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Payment not found"}, status=404)

    if invoice_tx.status == 'successful':
        return JsonResponse({
            "transaction_status": "successful"
        }, status=200)

    # Check if the current time has exceeded the completion time
    if timezone.now() > invoice_tx.completion_time:
        invoice_tx.status = 'expired'
        invoice_tx.success_url = f'{invoice_tx.payment_link}?transaction_id={invoice_tx.transaction_id}&status=expired'
        invoice_tx.save()
        return JsonResponse({"status": "expired", "message": "Invoice expired, please try again"}, status=400)
    
    # Increment the find_tx_counter
    invoice_tx.find_tx_counter += 1
    attempts = invoice_tx.find_tx_counter

    if attempts > 120:
        invoice_tx.status = 'expired'
        invoice_tx.success_url = f'{invoice_tx.payment_link}?transaction_id={invoice_tx.transaction_id}&status=expired'
        invoice_tx.save()
        return JsonResponse({"status": "expired", "message": "Invoice expired, please try again"}, status=400)
    
    print(f"Attempt {attempts}")

    invoice_tx.save()

    if invoice_tx.crypto_network == 'TRX':
        return handle_trx_transaction(invoice_tx)
    elif invoice_tx.crypto_network == 'TRC20':
        return handle_trc20_transaction(invoice_tx)
    else:
        return JsonResponse({'error': 'Unsupported crypto network.'}, status=400)


def handle_trx_transaction(invoice_tx):
    tx_amount = invoice_tx.converted_amount
    target_amount = tx_amount * 1000000
    api_url = invoice_tx.api_url
    created_at = invoice_tx.created_at.timestamp() * 1000  # Convert to milliseconds
    time_to_complete = invoice_tx.completion_time

    try:
        authorization = os.environ.get('TRON_PRO_API_KEY')
        headers = {
            'Content-Type': "application/json",
            'TRON-PRO-API-KEY': authorization
        }
        
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()

        for transaction in data['data']:
            if transaction['block_timestamp'] > created_at:  # Check if transaction occurred after created_at
                if transaction['ret'][0]['contractRet'] == 'SUCCESS':  # Check if contractRet is SUCCESS
                    for contract in transaction['raw_data']['contract']:
                        if 'parameter' in contract and 'value' in contract['parameter']:
                            if 'amount' in contract['parameter']['value'] and int(contract['parameter']['value']['amount']) == target_amount:
                                transaction_details = {
                                    'hash': transaction['txID'],
                                    'amount': contract['parameter']['value']['amount'],
                                    'confirmed': True,
                                }
                                return update_transaction_status(invoice_tx, transaction_details)

        return JsonResponse({'message': 'Transaction not found.'}, status=200)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def handle_trc20_transaction(invoice_tx):
    tx_amount = invoice_tx.converted_amount
    target_amount = math.floor(tx_amount * 1000000)
    api_url = invoice_tx.api_url
    created_at = invoice_tx.created_at.timestamp() * 1000  # Convert to milliseconds
    time_to_complete = invoice_tx.completion_time.timestamp() * 1000  # Convert to milliseconds

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        for transaction in data['data']:
            if int(transaction['value']) == target_amount and transaction['block_timestamp'] > created_at:
                transaction_details = {
                    'hash': transaction['transaction_id'],
                    'amount': target_amount,
                    'confirmed': True,
                }
                return update_transaction_status(invoice_tx, transaction_details)

        return JsonResponse({'message': 'Transaction not found.'}, status=200)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def update_transaction_status(invoice_tx, transaction_details):
    if transaction_details['confirmed']:
        try:
            invoice = Invoice.objects.get(invoice_id=invoice_tx)
            invoice.status = 'successful'
            invoice.is_paid = True
            invoice.save()
        except ObjectDoesNotExist:
            pass

        base_url = "https://tronscan.io/#/transaction/"
        invoice_tx.status = 'successful'
        invoice_tx.is_paid = True
        invoice_tx.business_name = invoice_tx.payment_link.tag_name
        invoice_tx.transaction_hash = f"{base_url}{transaction_details['hash']}"
        invoice_tx.success_url = f'{invoice_tx.success_url}?status=successful&transaction_id={invoice_tx.transaction_id}'
        invoice_tx.save()

        send_email(invoice_tx, invoice_tx.email, True)
        send_email(invoice_tx, invoice_tx.payment_link.user.email, False)

    return JsonResponse(transaction_details, status=200)




def create_invoice_view(request):

    # Fetch the payment links for the current user
    payment_links = PaymentLink.objects.filter(user=request.user)

    return render(request, 'home/create_invoice.html', {'payment_links': payment_links})


def create_invoice_via_storelink_view(request, link_id):

    # Fetch the payment links for the current user
    payment_links = PaymentLink.objects.filter(user=request.user)

    link_id = link_id

    context = {
        'payment_links': payment_links,
        'link_id': link_id,
    }

    # Pass the payment links to the template context
    return render(request, 'home/create_invoice.html', context)


@login_required
def save_invoice_view(request):    
    if request.method == 'POST':
        payment_link_id = request.POST.get('payment_link')
        try:
            payment_link = PaymentLink.objects.get(link_id=payment_link_id)
        except PaymentLink.DoesNotExist:
            messages.error(request, 'The selected payment link does not exist.')
            return redirect('create_invoice')
        
        recipient_email = request.POST.get('recipient_email')
        invoice_id = generate_random_string()
        amount = request.POST.get('amount')
        item = request.POST.get('item')
        item_quantity = request.POST.get('item_quantity')
        due_date = request.POST.get('due_date')

        save_invoice = Invoice.objects.create(
            user=request.user,
            payment_link=payment_link,
            recipient_email=recipient_email,
            invoice_id=invoice_id,
            amount=amount,
            item=item,
            item_quantity=item_quantity,
            due_date=due_date,
            invoice_url=f"/invoice/{invoice_id}",
        )
        save_invoice.save()

        payment = Payment.objects.create(
            user=payment_link.user,
            payment_link=payment_link,
            transaction_id=invoice_id,
            amount=amount,
            success_url=f"{request.get_host()}/invoice/{invoice_id}",
        )

        # Send email to recipient
        subject = f"Invoice from {payment_link.tag_name} #{invoice_id}"
        context = {
            'invoice': save_invoice,
            'payment_link': f"{request.get_host()}/invoice/{invoice_id}",
            'sender_name': payment_link.tag_name,
        }
        html_message = render_to_string('home/invoice_email_template.html', context)
        plain_message = strip_tags(html_message)
        from_email = settings.DEFAULT_FROM_EMAIL
        sender_name = "Bixmerchant Invoice"
        from_email_with_name = f"{sender_name} <{from_email}>"

        # Create and send the email
        msg = EmailMultiAlternatives(subject, plain_message, from_email_with_name, [recipient_email])
        msg.attach_alternative(html_message, "text/html")
        msg.send()

        messages.success(request, 'Your invoice has been created and sent to the recipient.')
        return redirect('show_all_invoices')

    return render(request, 'create_invoice.html')


@login_required
def show_all_invoices_view(request):
    invoices = Invoice.objects.filter(user=request.user)
    context = {
        'invoices': invoices
    }
    return render(request, 'home/view_invoices.html', context)


def store_pos_page_view(request, link_id):

    try:
        payment_link = get_object_or_404(PaymentLink, link_id=link_id)
        successful_payments = Payment.objects.filter(payment_link=payment_link, status='successful')
        total_successful_payments = successful_payments.aggregate(Sum('amount'))['amount__sum'] or 0

        context = {
            'payment_link': payment_link,
            'total_successful_payments': total_successful_payments,
        }
        
        return render(request, 'home/store_pos.html', context)
    
    except Http404:
        return render(request, 'home/invalid_pos.html', {'error_message': 'Payment link not found.'})


def pos_new_payment_view(request, link_id):

    payment_links = PaymentLink.objects.none()

    context = {
        'payment_links': payment_links,
        'link_id': link_id,
    }

    # Pass the payment links to the template context
    return render(request, 'home/new_pos_payment.html', context)


def pos_save_payment_view(request, link_id):    
    if request.method == 'POST':

        try:
            payment_link = PaymentLink.objects.get(link_id=link_id)
        except PaymentLink.DoesNotExist:
            messages.error(request, 'The selected payment link does not exist.')
            return redirect('pos_new_payment')
        
        tx_id = generate_random_string()
        get_amount = request.POST.get('amount')
        get_item = request.POST.get('item')

        payment = Payment.objects.create(
            user=payment_link.user,
            payment_link=payment_link,
            transaction_id=tx_id,
            amount=get_amount,
            item=get_item,
            # success_url = payment_link.callback_url,
            success_url = f"{request.get_host()}/pos/{payment_link.link_id}/tx_status/",
        )

        # Use the 'reverse' function to dynamically create the redirect URL
        redirect_url = reverse('select_transaction_crypto', kwargs={'tx_id': tx_id})
        return redirect(redirect_url)

    return redirect('pos_new_payment_view')


def pos_transactions_view(request, link_id):
    # Get the payment link or return a 404 error if not found
    payment_link = get_object_or_404(PaymentLink, link_id=link_id)
    
    # Get the transactions related to the payment link
    transactions = Payment.objects.filter(payment_link=payment_link)
    
    context = {
        'payment_link': payment_link,
        'transactions': transactions,
        'link_id': link_id,
    }

    # Pass the payment link and transactions to the template context
    return render(request, 'home/pos_transactions.html', context)

# Configure logging
logger = logging.getLogger(__name__)


def pos_payment_status(request, link_id):
    logger.debug("Received request for link_id: %s", link_id)
    transaction_id = request.GET.get('transaction_id')

    transaction_details = {}  # Initialize empty in case it needs to be passed without full details

    if not transaction_id:
        logger.error("Transaction ID is missing for link_id: %s", link_id)
        messages.error(request, "Transaction ID is missing.")
        return render(request, 'home/invalid_payment.html', {'link_id': link_id, 'transaction_details': transaction_details})

    try:
        payment_link = PaymentLink.objects.get(link_id=link_id)
    except PaymentLink.DoesNotExist:
        logger.error("Payment link not found for link_id: %s", link_id)
        messages.error(request, 'Store not found.')
        return render(request, 'home/invalid_payment.html', {'link_id': link_id, 'transaction_details': transaction_details})

    try:
        invoice = Payment.objects.get(transaction_id=transaction_id)
        logger.debug("Payment found: %s", invoice.transaction_id)
        # Update transaction_details with data available
        transaction_details = {
            'transaction_id': invoice.transaction_id,
            'link_id': payment_link.link_id,
            'amount': invoice.amount,
            'success_url': invoice.success_url,
            'created_at': invoice.created_at,
            'is_paid': invoice.is_paid,
            'status': invoice.status,
            'tag_name': payment_link.tag_name,
        }
    except Payment.DoesNotExist:
        logger.error("Payment not found for transaction_id: %s", transaction_id)
        messages.error(request, 'Transaction not found.')
        return render(request, 'home/pos_tx_error.html', {'link_id': link_id, 'transaction_details': transaction_details})

    # Successful retrieval of both Payment and PaymentLink
    context = {'transaction_details': transaction_details}
    
    logger.debug("Rendering successful transaction status for transaction_id: %s", transaction_id)
    return render(request, 'home/pos_tx_status.html', context)





















