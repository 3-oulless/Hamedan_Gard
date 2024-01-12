from django.urls import path
from . import views

app_name = "Account_Model"

urlpatterns = [
    path('send-otp/',views.SendOtpCode.as_view(),name='send_otp'),
    path('verify-otp/',views.VerifyOtpCode.as_view(),name='verify_otp'),
    path('register/',views.Register.as_view(),name='register'),

    path('login/',views.Login.as_view(),name='login'),

    path('profile/',views.ProfileView.as_view(),name='profile'),
]
