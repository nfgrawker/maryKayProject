from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login/homeLogin.html'), name='login'),
    path('forgotpassword/', views.forgotPassword),
    path("registeraccount/", views.registerAccount),
]
