from django.shortcuts import render
from django.views import View
from Services_Model.models import Hotel,Public_Parking,Restaurants,Villa,Tourism,Gallery_Villa_Picture,Count_Room_Hotel
from Contact_Us_Model.forms import ContactUserForm

class HomeView(View):

    def get(self,request):
        
        form = ContactUserForm()

        context = {
            'hotel_data' : Hotel.objects.all(),
            'parking_data' : Public_Parking.objects.all(),
            'rest_data' : Restaurants.objects.all(),
            'villa_data' : Villa.objects.all(),
            'tourism_data' : Tourism.objects.all(),
            'form' : form
        }
        return render(request,'Home/index.html',context)

class DetailView(View):

    def get(self,request,pk):

        context = {
            'data' : Tourism.objects.filter(pk=pk).first()
        }

        return render(request,'Detail/detail.html',context)

#-----Hotel-----
class Hotel_ListView(View):
    
    def get(self,request):
        context = {
            'hotel_list' : Hotel.objects.all(),
        }
        return render(request,'Hotel/list.html',context)
    
class DetailHotelView(View):

    def get(self,request,name):

        data_hotel = Hotel.objects.filter(name_en__iexact=name)
        count = Count_Room_Hotel.objects.filter(hotel_name=data_hotel.first()).first()
        context = {
            'data_hotel' : data_hotel,
            'count' : count
        }

        return render(request,'Hotel/detail.html',context)

#-----Restatunt-----
class Restaurant_ListView(View):
    
    def get(self,request):
        context = {
            'restaurant_list' : Restaurants.objects.all(),
        }
        return render(request,'Restaurants/list.html',context)

class DetailRestaurantView(View):

    def get(self,request,pk):
        context = {
            'data_res' : Restaurants.objects.filter(pk=pk).first()
        }
        print(Restaurants.objects.filter(pk=pk).first())
        return render(request,'Restaurants/detail.html',context)

#-----Villa-------
class Villa_ListView(View):
    
    def get(self,request):
        context = {
            'villa_list' : Villa.objects.all(),
        }
        return render(request,'Villa/list.html',context)
    
class DetailVillaView(View):

    def get(self,request,pk):

        data_villa = Villa.objects.filter(pk=pk).first()
        gallery_villa = Gallery_Villa_Picture.objects.filter(villa_type=data_villa)

        context = {
            'data_villa' : data_villa,
            'gallery_villa' : gallery_villa
        }
        return render(request,'Villa/detail.html',context)


class Public_Parking_ListView(View):
    
    def get(self,request):
        context = {
            'public_parking_list' : Public_Parking.objects.all(),
        }
        return render(request,'Public_Parking/list.html',context)
    
class DetailPublicParkingView(View):
    def get(self,request,pk):
        context = {
            'data_parking' : Public_Parking.objects.filter(pk=pk).first(),
        }
        return render(request,'Public_Parking/detail.html',context)


class SoghatView(View):

    def get(self,request):
        return render(request,'soghat.html')
