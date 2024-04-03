from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup_view, name='signup_page'),
    path('plans/', views.plan_view, name='plans'),
]
