from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
import string
import random
from django.utils import timezone

def generate_account_id():
    characters = string.ascii_letters + string.digits
    account_id = ''.join(random.choice(characters) for _ in range(12))
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
    

class PaymentLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link_id = models.CharField(max_length=20, unique=True, default=generate_account_id)
    # link = models.URLField(max_length=200)
    wallet = models.CharField(max_length=200, null=True, blank=True)
    crypto = models.CharField(max_length=200, null=True, blank=True)
    tag_name = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.link_id