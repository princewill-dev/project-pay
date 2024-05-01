from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('success/', views.success_page_view, name='success_page'),

    path('signup/', views.signup_view, name='signup_page'),

    path('login/', views.login_view, name='login_page'),

    path('logout/', views.logout_view, name='logout'),

    path('dashboard/', login_required(views.choose_action_view), name='choose_action'),

    path('create_payment_link/', login_required(views.create_payment_link_view), name='create_payment_link'),

    path('save_payment_link/', login_required(views.save_payment_link_view), name='save_payment_link'),

    path('transactions/', login_required(views.show_payments_view), name='payments'),

    path('my_payment_links/', login_required(views.pay_links_view), name='my_payment_links'),

    path('payment_link/<str:link_id>', login_required(views.payment_link_view), name='payment_link'),

    path('plans/', login_required(views.plan_view), name='plans'),

    path('email_verification/', views.email_verification_view, name='email_verification'),

    path('generate_otp/', views.generate_otp_view, name='generate_otp'),

    path('paylink/<str:link_id>', views.show_pay_link, name='get_pay_view'),

    path('api/generate_tx/<str:link_id>', views.generate_transaction_view, name='generate_transaction'),

]
