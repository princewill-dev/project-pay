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



def generate_random_string():
    random_string = ''.join(random.choice(string.digits) for _ in range(12))
    return random_string


def homepage(request):
    # return render(request, 'home/index.html')
    return render(request, 'landing/index.html')


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
        return redirect('plans')  # Redirect to 'plans' page
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save the user object yet
            otp_code = generate_otp()
            user.otp_code = otp_code
            user.otp_created_at = timezone.now()

            try:
                send_mail(
                    'Welcome to bitwade.com', 
                    f'Here is your email verification code: {otp_code}',
                    'support@bitwade.com',
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
    return redirect('login_page')


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

                qr_code_image = generate_qr_code(wallet_address)

                filename = f'{wallet_address}_{payment_link.link_id}.png'

                qr_code_image_file = ContentFile(qr_code_image.getvalue(), name=filename)

                Wallet.objects.create(
                    user=request.user,
                    wallet_id=payment_link,
                    crypto=token.token_tag,
                    address=wallet_address,
                    qr_code_image=qr_code_image_file,
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
        link_description = request.POST.get('link_description')
        link_id = generate_random_string()

        # Create a PaymentLink instance
        payment_link = PaymentLink.objects.create(
            user=request.user,
            link_id=link_id,
            tag_name=tag_name,
            link_logo=content_file,
            link_url=link_url,
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

                filename = f'{wallet_address}_{payment_link.link_id}.png'

                qr_code_image_file = ContentFile(qr_code_image.getvalue(), name=filename)

                Wallet.objects.create(
                    user=request.user,
                    wallet_id=payment_link,
                    crypto=token.token_tag,
                    address=wallet_address,
                    qr_code_image=qr_code_image_file,
                )

        messages.success(request, 'Your store link has been created.')
        return redirect('show_all_payment_links')

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
        if content_file is not None:  # Only assign content_file to link_logo if content_file is not None
            payment_link.link_logo = content_file
        payment_link.link_description = request.POST.get('link_description')
        payment_link.save()

        # Get the Wallet instances associated with the PaymentLink
        # wallets = Wallet.objects.filter(wallet_id=payment_link)

        # # Update each Wallet instance
        # for wallet in wallets:
        #     wallet_address = request.POST.get(f'{wallet.crypto}wallet')
        #     if wallet_address:
        #         qr_code_image = generate_qr_code(wallet_address)
        #         filename = f'{wallet_address}.png'
        #         path = default_storage.save(filename, ContentFile(qr_code_image.getvalue()))
        #         wallet.qr_code_image = path
        #         wallet.address = wallet_address
        #         wallet.save()

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
    


@csrf_exempt
@require_http_methods(['POST'])
def transaction_checkout_view(request):

    CUSTOM_API_KEY_HEADER = 'BITWADE-API-KEY'  # Replace with your desired custom header name
    CUSTOM_API_KEY_HEADER = CUSTOM_API_KEY_HEADER.replace('-', '_').upper()  # Convert to Django's header format

    if request.method == 'POST':
        api_key = request.META.get(f'HTTP_{CUSTOM_API_KEY_HEADER}')
        if not api_key:
            return JsonResponse({"error": "No API key provided in the headers"}, status=400)

        try:
            payment_link = PaymentLink.objects.get(api_key=api_key)
        except PaymentLink.DoesNotExist:
            return JsonResponse({"error": "Invalid API key"}, status=403)

        data = json.loads(request.body)
        try:
            payment = Payment.objects.create(
                user=payment_link.user,
                payment_link=payment_link,
                transaction_id=generate_random_string(),
                amount=data['amount'],
                customer_email=data['email'],
                success_url=data['success_url'],
            )
            return JsonResponse({
                "status": True,
                "amount": data['amount'],
                "message": "payment generated successfully",
                "created_at": payment.created_at,
                "transaction_id": payment.transaction_id,
                "transaction_url": f"{request.get_host()}/invoice/{payment.transaction_id}",
            }, status=201)
        except IntegrityError as e:
            return JsonResponse({"error": f"Failed to create payment: {str(e)}"}, status=500)
    else:
        return HttpResponse(status=405)
    

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

    
def save_crypto_selection_view(request, tx_id):

    invoice_id = get_object_or_404(Payment, transaction_id=tx_id)

    if request.method == 'POST':
        
        selected_crypto = request.POST.get('selected_crypto')

        wallet = invoice_id.payment_link.wallet_set.filter(crypto=selected_crypto).first()

        targeted_address = wallet.address

        amount_in_usd = invoice_id.amount

        amount_in_trx = convert_usd_to_trx(amount_in_usd)

        if selected_crypto == 'trx':

            api_link = f'https://api.trongrid.io/v1/accounts/{targeted_address}/transactions/'

            converted_amt = amount_in_trx

        elif selected_crypto == 'trc20':

            api_link = f'https://api.trongrid.io/v1/accounts/{targeted_address}/transactions/trc20?limit=100&contract_address=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t'

            converted_amt = amount_in_usd

        # Update the database where this transaction exists
        invoice_id.crypto_network = selected_crypto
        invoice_id.wallet_address = wallet.address
        invoice_id.converted_amount = converted_amt
        invoice_id.api_url = api_link
        invoice_id.save()

        return redirect('make_payment_page', tx_id=invoice_id.transaction_id)

    # Handle GET requests
    return redirect('select_transaction_crypto', tx_id=invoice_id.transaction_id)


def select_transaction_crypto_view(request, tx_id):

    try:
        # Get the Payment object with the given transaction ID
        invoice_id = Payment.objects.get(transaction_id=tx_id)

        if invoice_id.status == 'successful':

            transaction_details = {
                'transaction_id': invoice_id.transaction_id,
                'payment_link': invoice_id.payment_link.link_id,
                'amount': invoice_id.amount,
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

        # Get the crypto and address connected to the transaction
        crypto_networks = Wallet.objects.filter(wallet_id=payment_link)
        if crypto_networks.exists():
            available_cryptos = list(crypto_networks.values_list('crypto', flat=True))
        else:
            # Handle the case when the wallet does not exist
            available_cryptos = "Unknown"

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
        # messages.error(request, 'Transaction not found.')
        return render(request, 'home/invalid_payment.html')

    

def make_payment_view(request, tx_id):

    try:

        invoice_id = Payment.objects.get(transaction_id=tx_id)

        selected_crypto = invoice_id.crypto_network

        print(selected_crypto)

        targeted_address = invoice_id.wallet_address

        find_qrcode_image = Wallet.objects.filter(address=targeted_address).first()

        qr_code = find_qrcode_image.qr_code_image

        transaction_details = {
            'transaction_id': invoice_id.transaction_id,
            'payment_link': invoice_id.payment_link.link_id,
            'amount': invoice_id.amount,
            'converted_amount': invoice_id.converted_amount,
            'success_url': invoice_id.success_url,
            'created_at': invoice_id.created_at,
            'is_paid': invoice_id.is_paid,
            'status': invoice_id.status,
            'tag_name': invoice_id.payment_link.tag_name,
            'wallet': targeted_address,
            'crypto_network': selected_crypto,
            'qr_code': qr_code,
        }

        context = {
            'transaction_details': transaction_details,
        }
        return render(request, 'home/make_payment.html', context)
    
    except Payment.DoesNotExist:
        # Render the error page if the Payment object does not exist
        # messages.error(request, 'Transaction not found.')
        return render(request, 'home/invalid_payment.html')
  

def blockchain_api_view(request, tx_id):

    invoice_tx = Payment.objects.get(transaction_id=tx_id)

    

    if invoice_tx.crypto_network == 'trx':

        tx_amount = invoice_tx.converted_amount

        target_amount = tx_amount * 1000000

        api_url = invoice_tx.api_url        

        max_attempts = 5
        attempts = 0

        try:
            
            while attempts < max_attempts:
                try:

                    import os
                    import environ
                    env = environ.Env()
                    environ.Env.read_env()

                    authorization = os.environ.get('TRON_PRO_API_KEY')

                    url = api_url

                    headers = {
                        'Content-Type': "application/json",
                        'TRON-PRO-API-KEY': authorization
                    }
                    
                    response = requests.get(url, headers=headers)
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
                                            try:
                                                # Check if the transaction exists in the Invoice model
                                                invoice = Invoice.objects.get(invoice_id=invoice_tx)
                                                # If it exists, mark it as successful
                                                invoice.status = 'successful'
                                                invoice.is_paid = True
                                                # send email to the recipient and the sender
                                                invoice.save()
                                            except ObjectDoesNotExist:
                                                pass
                                            
                                            base_url = "https://tronscan.io/#/transaction/"
                                            invoice_tx.status = 'successful'
                                            invoice_tx.is_paid = True
                                            invoice_tx.business_name = invoice_tx.payment_link.tag_name
                                            invoice_tx.transaction_hash = f"{base_url}{transaction_details['hash']}"
                                            invoice_tx.business_name = invoice_tx.payment_link.tag_name
                                            invoice_tx.save()

                                            # send email to the recipient and the sender

                                        return JsonResponse(transaction_details)

                    attempts += 1

                except requests.exceptions.RequestException as e:
                    return JsonResponse({'error': str(e)}, status=500)

            return JsonResponse({'error': 'Target amount not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
    elif invoice_tx.crypto_network == 'trc20':

        tx_amount = invoice_tx.converted_amount
        target_amount = math.floor(tx_amount * 1000000)

        print(target_amount)

        api_url = invoice_tx.api_url
        max_attempts = 5
        attempts = 0

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()

            for transaction in data['data']:
                if int(transaction['value']) == target_amount:

                    try:
                        # Check if the transaction exists in the Invoice model
                        invoice = Invoice.objects.get(invoice_id=invoice_tx)
                        # If it exists, mark it as successful
                        invoice.status = 'successful'
                        invoice.is_paid = True
                        # send email to the recipient and the sender
                        invoice.save()
                    except ObjectDoesNotExist:
                        pass

                    base_url = "https://tronscan.io/#/transaction/"
                    invoice_tx.status = 'successful'
                    invoice_tx.is_paid = True
                    invoice_tx.business_name = invoice_tx.payment_link.tag_name
                    invoice_tx.transaction_hash = f"{base_url}{transaction['transaction_id']}"
                    invoice_tx.business_name = invoice_tx.payment_link.tag_name
                    invoice_tx.save()

                    return JsonResponse({
                        'hash': transaction['transaction_id'],
                        'amount': target_amount,
                        'confirmed': True
                    })

            return JsonResponse({'error': 'Transaction not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    

# def create_invoice_view(request):
#     return render(request, 'home/create_invoice.html')


def create_invoice_view(request):
    # Fetch the payment links for the current user
    payment_links = PaymentLink.objects.filter(user=request.user)

    # Pass the payment links to the template context
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
        # payment_link = request.POST.get('payment_link')
        # payment_link_id = request.POST.get('payment_link')
        # payment_link = PaymentLink.objects.get(id=payment_link_id)

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
            success_url=f"/store/success/",
        )


    messages.success(request, 'Your invoice has been created.')
    return redirect('show_all_invoices')


@login_required
def show_all_invoices_view(request):
    invoices = Invoice.objects.filter(user=request.user)
    context = {
        'invoices': invoices
    }
    return render(request, 'home/view_invoices.html', context)