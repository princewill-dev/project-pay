from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from .models import User, PaymentLink, Payments
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




















# def generate_random_string(length=20):
#     characters = string.ascii_lowercase + string.digits
#     random_string = ''.join(random.choice(characters) for _ in range(length))
#     return random_string

# def generate_random_string():
#     random_string = ''.join(random.choice(string.digits) for _ in range(12))
#     formatted_string = '-'.join([random_string[i:i+4] for i in range(0, len(random_string), 4)])
#     return formatted_string


def generate_random_string():
    random_string = ''.join(random.choice(string.digits) for _ in range(12))
    return random_string



def homepage(request):
    return render(request, 'home/index.html')


def success_page_view(request):
    return render(request, 'home/temp_success_page.html')


def email_verification_view(request):
    return render(request, 'home/verify.html')


def plans_view(request):
    return render(request, 'home/pricing_plan.html')


def dashboard_view(request):
    payment_links = PaymentLink.objects.filter(user=request.user)
    print(payment_links.count())
    payments = Payments.objects.filter(user=request.user)
    print(payments.count())
    account_id = request.user.account_id
    context = {
        'payments': payments,
        'payment_links': payment_links,
        'account_id': account_id,
    }
    return render(request, 'home/dashboard.html', context)


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
                return redirect('dashboard')
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


def create_payment_link_view(request):
    return render(request, 'home/create_payment_link.html')


@login_required
def save_payment_link_view(request):    
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
    return redirect('show_all_payment_links')


# shows all payments made to the user
@login_required
def show_transactions_view(request):
    transactions = Payments.objects.filter(user=request.user)
    context = {
        'transactions': transactions,
    }
    return render(request, 'home/transactions_table.html', context)


# shows individual payment link created by a user
def show_payment_link_view(request, link_id):
    instance = get_object_or_404(PaymentLink, link_id=link_id)
    context = {
        'instance': instance,
    }
    return render(request, 'home/show_payment_link.html', context)


# Get all the payment links created by the current user
@login_required
def show_all_payment_links_view(request):
    payment_links = PaymentLink.objects.filter(user=request.user)
    context = {
        'payment_links': payment_links
    }
    return render(request, 'home/payment_links.html', context)


@login_required
def delete_payment_link_view(request, link_id):
    payment_link = get_object_or_404(PaymentLink, link_id=link_id, user=request.user)
    payment_link.delete()
    messages.success(request, 'Payment link deleted successfully.')
    return redirect('show_all_payment_links')


# @login_required
# def payment_link_view(request, link_id):
#     instance = get_object_or_404(PaymentLink, link_id=link_id)
#     return render(request, 'home/payment_link.html', {'instance': instance})


@csrf_exempt
def generate_transaction_view(request, link_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            payment_link = PaymentLink.objects.get(link_id=link_id)
        except PaymentLink.DoesNotExist:
            return JsonResponse({"error": "Invalid payment link ID"}, status=400)

        try:
            payment = Payments.objects.create(
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


def get_transaction_view(request, tx_id):
    # Get the Payments object with the given transaction ID
    invoice_tx = get_object_or_404(Payments, transaction_id=tx_id)

    # Get the transaction details
    transaction_details = {
        'transaction_id': invoice_tx.transaction_id,
        'payment_link': invoice_tx.payment_link.link_id,
        'amount': invoice_tx.amount,
        'success_url': invoice_tx.success_url,
        'created_at': invoice_tx.created_at,
        'is_paid': invoice_tx.is_paid,
        'status': invoice_tx.status,
    }

    # Get the user's information
    user_info = {
        'tag_name': invoice_tx.payment_link.tag_name,
        'wallet': invoice_tx.payment_link.wallet,
        'crypto': invoice_tx.payment_link.crypto,
        'qr_code_image': invoice_tx.payment_link.qr_code_image.url if invoice_tx.payment_link.qr_code_image else '',
        
        # Add other user info here...
    }

    # Combine the user info and transaction details into one context
    context = {
        'user_info': user_info,
        'transaction_details': transaction_details,
    }

    # Render the context to a template
    return render(request, 'home/get_transaction.html', context)


# def get_transaction_details(request, tx_id):

#     invoice_tx = get_object_or_404(Payments, transaction_id=tx_id)

#     target_amount = invoice_tx.amount

#     target_wallet = invoice_tx.payment_link.wallet

#     # Get the API endpoint URL from your Django settings
#     api_url = f'https://apilist.tronscanapi.com/api/transfer/trx?address={target_wallet}&start=0&limit=20&direction=0&reverse=true&fee=true&db_version=1&start_timestamp=&end_timestamp='

#     while True:
#         try:
#             # Make a GET request to the API endpoint
#             response = requests.get(api_url)
#             response.raise_for_status()

#             # Parse the JSON response
#             data = response.json()

#             # Check if the target amount is present in the response data
#             for transaction in data['data']:
#                 if int(transaction['amount']) == target_amount:
#                     # If the target amount is found, return the transaction details
#                     transaction_details = {
#                         'hash': transaction['hash'],
#                         'amount': transaction['amount'],
#                         'confirmed': transaction['confirmed'],
#                     }
#                     json_data = json.dumps(transaction_details)
#                     return HttpResponse(json_data, content_type='application/json')

#             # If the target amount is not found, sleep for a few seconds before checking again
#             time.sleep(5)

#         except requests.exceptions.RequestException as e:
#             # Handle any exceptions that occur during the API request
#             error_response = {'error': str(e)}
#             json_data = json.dumps(error_response)
#             return HttpResponse(json_data, content_type='application/json', status=500)



    

def get_transaction_details(request, tx_id):
    try:
        invoice_tx = get_object_or_404(Payments, transaction_id=tx_id)
        target_amount = invoice_tx.amount * 1000000
        target_wallet = invoice_tx.payment_link.wallet

        api_url = f'https://api.trongrid.io/v1/accounts/{target_wallet}/transactions/'

        max_attempts = 5
        attempts = 0

        while attempts < max_attempts:
            try:
                response = requests.get(api_url)
                response.raise_for_status()

                data = response.json()

                for transaction in data['data']:
                    if 'contract' in transaction['raw_data']:
                        for contract in transaction['raw_data']['contract']:
                            if 'parameter' in contract and 'value' in contract['parameter']:
                                if 'amount' in contract['parameter']['value'] and int(contract['parameter']['value']['amount']) == target_amount:
                                    transaction_details = {
                                        'hash': transaction['txID'],
                                        'amount': contract['parameter']['value']['amount'],
                                        'confirmed': transaction['ret'][0]['contractRet'] == 'SUCCESS',
                                    }
                                    if transaction_details['confirmed']:
                                        invoice_tx.status = 'successful'
                                        invoice_tx.is_paid = True
                                        invoice_tx.crypto_network = 'TRON'
                                        invoice_tx.business_name = invoice_tx.payment_link.tag_name
                                        invoice_tx.transaction_hash = transaction_details['hash']
                                        invoice_tx.business_name = invoice_tx.payment_link.tag_name
                                        invoice_tx.save()
                                    return JsonResponse(transaction_details)

                attempts += 1

            except requests.exceptions.RequestException as e:
                return JsonResponse({'error': str(e)}, status=500)

        return JsonResponse({'error': 'Target amount not found.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    

def create_invoice_view(request):
    return render(request, 'home/create_invoice.html')






