from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('accounts/signup/', views.signup_view, name='signup_page'),
    path('accounts/login/', views.login_view, name='login_page'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/dashboard/', login_required(views.choose_action_view), name='choose_action'),
    path('accounts/create_payment/', login_required(views.create_payment_view), name='create_payment'),
    path('accounts/create_payment_save/', login_required(views.create_payment_save), name='create_payment_save'),
    path('accounts/pay_links/', login_required(views.pay_links_view), name='pay_links'),
    path('accounts/payment_link/<str:link_id>', login_required(views.payment_link_view), name='payment_link'),
    path('accounts/plans/', login_required(views.plan_view), name='plans'),
    path('accounts/email_verification/', views.email_verification_view, name='email_verification'),
    path('generate_otp/', views.generate_otp_view, name='generate_otp'),
    path('pay/<str:link_id>', views.get_pay_view, name='get_pay_view'),
    # path('accounts/create_invoice/', login_required(views.create_invoice_view), name='create_invoice'),
    path('api/generate_tx/<str:link_id>', views.generate_transaction_view, name='generate_transaction'),

]
