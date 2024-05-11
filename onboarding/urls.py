from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

urlpatterns = [

    path('', views.homepage, name='homepage'),

    path('store/success/', views.success_page_view, name='success_page'),

    path('signup/', views.signup_view, name='signup_page'),

    path('generate_otp/', views.generate_otp_view, name='generate_otp'),

    path('email_verification/', views.email_verification_view, name='email_verification'),

    path('plans/', login_required(views.plans_view), name='plans'),

    path('login/', views.login_view, name='login_page'),

    path('dashboard/', login_required(views.dashboard_view), name='dashboard'),

    path('logout/', views.logout_view, name='logout'),

    path('create_payment_link/', login_required(views.create_payment_link_view), name='create_payment_link'),

    path('delete_payment_link/<str:link_id>', login_required(views.delete_payment_link_view), name='delete_payment_link'),

    path('edit_payment_link/<str:link_id>', login_required(views.edit_payment_link_wallet_view), name='edit_payment_link_wallet'),

    path('save_payment_link/', login_required(views.save_payment_link_view), name='save_payment_link'),

    path('payment_links/', login_required(views.show_all_payment_links_view), name='show_all_payment_links'),

    path('transactions/', login_required(views.show_transactions_view), name='show_transactions'),

    # path('payment_link/<str:link_id>', login_required(views.payment_link_view), name='payment_link'),

    path('paylink/<str:link_id>', views.show_payment_link_view, name='show_payment_link'),

    path('generate/<str:link_id>', views.generate_transaction_view, name='generate_transaction'),

    path('invoice/<str:tx_id>', views.select_transaction_crypto_view, name='select_transaction_crypto'),

    path('invoice/<str:tx_id>', require_http_methods(['POST'])(views.save_invoice_view), name='save_invoice'),

    path('crypto_selection/<str:tx_id>', views.save_crypto_selection_view, name='save_crypto_selection'),

    path('blockchain_api/<str:tx_id>', views.blockchain_api_view, name='blockchain_api'),

    path('create_invoice/', login_required(views.create_invoice_view), name='create_invoice'),

    path('save_invoice/', login_required(views.save_invoice_view), name='save_invoice'),

    path('invoices/', login_required(views.show_all_invoices_view), name='show_all_invoices'),

    path('pay/<str:tx_id>', views.make_payment_view, name='make_payment_page'),



]
