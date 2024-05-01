from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('', views.homepage, name='homepage'),

    path('success/', views.success_page_view, name='success_page'),

    path('signup/', views.signup_view, name='signup_page'),

    path('generate_otp/', views.generate_otp_view, name='generate_otp'),

    path('email_verification/', views.email_verification_view, name='email_verification'),

    path('plans/', login_required(views.plans_view), name='plans'),

    path('login/', views.login_view, name='login_page'),

    path('dashboard/', login_required(views.dashboard_view), name='dashboard'),

    path('logout/', views.logout_view, name='logout'),

    path('create_payment_link/', login_required(views.create_payment_link_view), name='create_payment_link'),

    path('save_payment_link/', login_required(views.save_payment_link_view), name='save_payment_link'),

    path('payment_links/', login_required(views.show_all_payment_links_view), name='show_all_payment_links'),

    path('transactions/', login_required(views.show_transactions_view), name='show_transactions'),

    # path('payment_link/<str:link_id>', login_required(views.payment_link_view), name='payment_link'),

    path('paylink/<str:link_id>', views.show_payment_link_view, name='show_payment_link'),

    path('api/generate_tx/<str:link_id>', views.generate_transaction_view, name='generate_transaction'),

    path('tx/<str:tx_id>', views.get_transaction_view, name='get_transaction'),

]
