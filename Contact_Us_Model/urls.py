from django.urls import path
from . import views

app_name = "Contact_Us_Model"

urlpatterns = [
    path("",views.ContactUsView.as_view(),name="ContactUs")
]
