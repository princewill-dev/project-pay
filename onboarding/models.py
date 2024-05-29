from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
import string
import random
from django.utils import timezone
from django.db.models import JSONField
import secrets




def generate_account_id():
    account_id = ''.join(random.choice(string.digits) for _ in range(12))
    return account_id

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

    def delete_user(self, email):
        user = self.get(email=email)
        user.delete()

class User(AbstractBaseUser, PermissionsMixin):
    account_id = models.CharField(max_length=12, unique=True, default=generate_account_id)
    email = models.EmailField(_('email address'), unique=True)
    email_verification = models.CharField(default='unverified', max_length=255)
    otp_code = models.CharField(max_length=6, null=True, blank=True)
    otp_created_at = models.DateTimeField(null=True, blank=True)
    otp_verified_at = models.DateTimeField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_name='custom_user_set',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='custom_user_set',
        related_query_name='user',
    )

    def __str__(self):
        return self.email


class Token(models.Model):
    token_id = models.CharField(max_length=200, null=True, blank=True, unique=True)
    token_logo = models.FileField(upload_to='token_logos', blank=True, null=True)
    token_name = models.CharField(max_length=200, null=True, blank=True)
    token_tag = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.token_id
    

class PaymentLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link_id = models.CharField(max_length=200, null=True, blank=True, unique=True)
    link_logo = models.FileField(upload_to='link_logos', blank=True, null=True)
    tag_name = models.CharField(max_length=200, null=True, blank=True)
    link_url = models.URLField(null=True, blank=True)
    link_description = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    link_ip_address = models.GenericIPAddressField(null=True, blank=True)
    link_user_agent = models.CharField(max_length=200, null=True, blank=True)
    link_country = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    api_key = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.link_id

    def save(self, *args, **kwargs):
        # If the PaymentLink instance doesn't have an API key, generate one
        if not self.api_key:
            self.api_key = secrets.token_urlsafe(24)  # Generate a 24-character secure random string
        super().save(*args, **kwargs)
    

class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet_id = models.ForeignKey(PaymentLink, null=True, on_delete=models.CASCADE)  # Change this line
    crypto = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200)
    qr_code_image = models.FileField(upload_to='qr_codes/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Wallet for {self.user.email}"
    

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_link = models.ForeignKey(PaymentLink, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=200) # expected in API call
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    converted_amount = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    random_added_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    item = models.CharField(max_length=200, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True) # expected in API call
    crypto_network = models.CharField(max_length=200,null=True, blank=True)
    wallet_address = models.CharField(max_length=200,null=True, blank=True)
    transaction_hash = models.CharField(max_length=200, null=True, blank=True)
    api_url = models.CharField(max_length=200, null=True, blank=True)
    business_name = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_paid = models.BooleanField(default=False)
    success_url = models.URLField(null=True)
    status = models.CharField(max_length=200, default='pending')
    find_tx_counter = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.transaction_id
    

class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_link = models.ForeignKey(PaymentLink, on_delete=models.CASCADE)
    invoice_id = models.CharField(max_length=200, unique=True)
    recipient_email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    item = models.CharField(max_length=200)
    item_quantity = models.IntegerField()
    due_date = models.DateField()
    invoice_url = models.URLField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=200, default='pending')
    
    def __str__(self):
        return self.invoice_id