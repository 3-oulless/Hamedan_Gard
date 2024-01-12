from django.urls import path
from . import views

app_name = "Home_Model"

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('tourism/<pk>/',views.DetailView.as_view(),name='Detail'),
    path('hotel-list/',views.Hotel_ListView.as_view(),name='Hotel_list'),
    path('hotel/<name>/',views.DetailHotelView.as_view(),name='Hotel_detail'),
    path('res-list/',views.Restaurant_ListView.as_view(),name='res_list'),
    path('res/<pk>',views.DetailRestaurantView.as_view(),name='res_detail'),
    path('villa-list/',views.Villa_ListView.as_view(),name='villa_list'),
    path('villa/<pk>',views.DetailVillaView.as_view(),name='villa_detail'),
    path('parking-list/',views.Public_Parking_ListView.as_view(),name='parking_list'),
    path('parking/<pk>',views.DetailPublicParkingView.as_view(),name='parking_detail'),
    path('soghati/',views.SoghatView.as_view(),name='soghat'),
]
