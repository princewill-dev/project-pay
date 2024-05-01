from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, PaymentLink, Payments

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
    list_display = ('link_id', 'user', 'tag_name', 'crypto', 'wallet', 'created_at', 'is_active')
    search_fields = ('user__email', 'link_id')
    list_filter = ('is_active', 'created_at')


class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'user', 'payment_link', 'amount', 'created_at', 'is_paid', 'status')
    search_fields = ('user__email', 'payment_link__link_id')
    list_filter = ('created_at', 'transaction_id')



admin.site.register(User, UserAdmin)
admin.site.register(PaymentLink, PaymentLinkAdmin,)
admin.site.register(Payments, PaymentsAdmin)