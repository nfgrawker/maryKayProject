from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.homeLogin, name = "loginHome"),
    path('forgotpassword/', views.forgotPassword),
    path("registeraccount/", views.registerAccount),

]
