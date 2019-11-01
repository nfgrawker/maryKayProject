from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login/homeLogin.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='/login/logout.html'), name='logout'),
    path('forgotpassword/', views.forgotPassword),
    path("registeraccount/", views.registerAccount),
    path("", views.mainRedirect),
]
