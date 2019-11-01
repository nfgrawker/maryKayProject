from django.urls import path, include
from . import views

urlpatterns = [
    path('forgotpassword/', views.forgotPassword),
    path("registeraccount/", views.registerAccount),
    path("", views.mainRedirect),
    path("logout/", views.logout_view),
]
