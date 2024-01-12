from django.urls import path,include
from . import views

app_name = "Reservation_Model"

urlpatterns = [
    path('hotel',views.ReservationHotelView,name='Reservation_Hotel'),
    path('villa',views.ReservationVillaView,name='Reservation_Villa'),

    path('delete-hotel',views.RemoveReservationHotelView,name='Delete_Reservation_Hotel'),
    path('delete-villa',views.RemoveReservationVillaView,name='Delete_Reservation_villa'),

]
