from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('accounts/signup/', views.signup_view, name='signup_page'),
    path('accounts/login/', views.login_view, name='login_page'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/plans/', login_required(views.plan_view), name='plans'),
    path('accounts/email_verification/', views.email_verification_view, name='email_verification'),
    path('generate_otp/', views.generate_otp_view, name='generate_otp'),
]
