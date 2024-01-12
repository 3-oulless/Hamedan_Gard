from django.shortcuts import render,redirect
from .models import ContactUs
from django.views import View
from .forms import ContactUserForm
from Services_Model.models import Hotel,Public_Parking,Restaurants,Villa,Tourism,Gallery_Villa_Picture,Count_Room_Hotel

class ContactUsView(View):

    def post(self,request):

        form = ContactUserForm(request.POST or None)

        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            comment = form.cleaned_data.get('comment')

            ContactUs.objects.create(full_name=full_name, email=email, subject=subject, comment=comment)

            return redirect('Home_Model:home')

        context = {
            'hotel_data' : Hotel.objects.all(),
            'parking_data' : Public_Parking.objects.all(),
            'rest_data' : Restaurants.objects.all(),
            'villa_data' : Villa.objects.all(),
            'tourism_data' : Tourism.objects.all(),
            'form' : form
        }
        return render(request,'Home/index.html',context)


