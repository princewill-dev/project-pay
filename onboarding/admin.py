from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, PaymentLink, Payment, Invoice
from .models import User, PaymentLink, Payment, Invoice, Wallet
from .models import Token




class UserAdmin(BaseUserAdmin):
    list_display = ('account_id', 'email', 'email_verification', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('account_id', 'email', 'password', 'otp_code', 'otp_created_at', 'otp_verified_at')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'otp_code', 'otp_created_at')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class PaymentLinkAdmin(admin.ModelAdmin):
    list_display = ('link_id', 'user', 'tag_name', 'created_at', 'is_active')
    search_fields = ('user__email', 'link_id')
    list_filter = ('is_active', 'created_at')


class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'user', 'payment_link', 'amount', 'created_at', 'is_paid', 'status')
    search_fields = ('user__email', 'payment_link__link_id')
    list_filter = ('created_at', 'transaction_id')


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_id', 'user', 'payment_link', 'amount', 'recipient_email', 'item', 'item_quantity', 'due_date', 'created_at', 'is_paid', 'status')
    search_fields = ('invoice_id', 'user__email', 'payment_link__link_id')
    list_filter = ('created_at', 'invoice_id')


class WalletAdmin(admin.ModelAdmin):
    list_display = ('wallet_id', 'user', 'crypto', 'address', 'created_at')
    search_fields = ('user__email',)
    list_filter = ('user',)


class TokenAdmin(admin.ModelAdmin):
    list_display = ('token_id', 'token_name', 'token_tag', 'created_at', 'is_active')
    search_fields = ('token_id', 'token_name', 'token_tag')
    list_filter = ('is_active', 'created_at')

admin.site.register(Token, TokenAdmin)





admin.site.register(Wallet, WalletAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(PaymentLink, PaymentLinkAdmin,)
admin.site.register(Payment, PaymentsAdmin)
admin.site.register(Invoice, InvoiceAdmin)