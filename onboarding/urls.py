from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup_view, name='signup_page'),
    path('login/', views.login_view, name='login_page'),
    path('logout/', views.logout_view, name='logout'),
    path('plans/', views.plan_view, name='plans'),
    path('email_verification/', views.email_verification_view, name='email_verification'),
    
]
