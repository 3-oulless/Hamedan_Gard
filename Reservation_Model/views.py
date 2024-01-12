from django.shortcuts import render,redirect
from Account_Model.models import User
from Services_Model.models import Hotel,Villa,Count_Room_Hotel
from .models import Reservation_Hotel,Reservation_Villa
from django.views import View
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required




@login_required()
def ReservationHotelView(request):
    user_id = request.GET.get('user_id')
    hotel_id = request.GET.get('hotel_id')
    count = int(request.GET.get('count'))
    date = request.GET.get('date')

    print(date)

    if count < 1:
        return JsonResponse({
           'status' : 'invalid_count',
            'title': 'اعلان',
            'text': "تعداد روز مشخص شده نامعتبر است",
            'icon': 'error',
            'confirmButtonColor': '#3085d6',
            'confirmButtonText': 'باشه ممنون' 
        })
    
    if request.user.is_authenticated:
        date_hotel = Hotel.objects.filter(id=hotel_id).first()
        date_user = User.objects.filter(id=user_id).first()
        data_count = Count_Room_Hotel.objects.filter(hotel_name=date_hotel).first()

        if date_hotel is not None or date_user is not None:
            price = int(count) * date_hotel.price
            Reservation_Hotel.objects.create(user_id=user_id, hotel_id=hotel_id,in_hotel=date, price=price,count=count)
            date_hotel.status = True
            count = data_count.count_room
            count = count - 1
            data_count.count_room = count
            data_count.save()

            date_hotel.save()
            return JsonResponse({
                'status' : 'success',
                'title': 'اعلان',
                'text': "اتاق شما با موفقیت رزرو شد",
                'icon': 'success',
                'confirmButtonText': 'باشه ممنون'
            })
        else:
            return JsonResponse({
                'status' : 'not_found',
                'title': 'اعلان',
                'text': "اطلاعات وارد شده صحیح نمی باشد",
                'icon': 'error',
                'confirmButtonColor': '#3085d6',
                'confirmButtonText': 'باشه ممنون'
            })
    else:
        return JsonResponse({
            'status' : 'not_auth',
            'title': 'اعلان',
            'text': "لطفا ابتدا وارد حساب کاربری خود شوید",
            'icon': 'error',
            'confirmButtonColor': '#3085d6',
            'confirmButtonText': 'باشه ممنون'
            })



@login_required()
def ReservationVillaView(request):
    user_id = request.GET.get('user_id')
    villa_id = request.GET.get('villa_id')
    count = int(request.GET.get('count'))
    date = request.GET.get('date')

    print(date)

    if count < 1:
        return JsonResponse({
           'status' : 'invalid_count',
            'title': 'اعلان',
            'text': "تعداد روز مشخص شده نامعتبر است",
            'icon': 'error',
            'confirmButtonColor': '#3085d6',
            'confirmButtonText': 'باشه ممنون' 
        })
    
    if request.user.is_authenticated:
        date_villa = Villa.objects.filter(id=villa_id).first()
        date_user = User.objects.filter(id=user_id).first()

        if date_villa is not None or date_user is not None:
            price = int(count) * date_villa.price
            Reservation_Villa.objects.create(user_id=user_id, Villa_id=villa_id,in_hotel=date, price=price,count=count)
            date_villa.status = True
            date_villa.save()

            return JsonResponse({
                'status' : 'success',
                'title': 'اعلان',
                'text': "اتاق شما با موفقیت رزرو شد",
                'icon': 'success',
                'confirmButtonText': 'باشه ممنون'
            })
        else:
            return JsonResponse({
                'status' : 'not_found',
                'title': 'اعلان',
                'text': "اطلاعات وارد شده صحیح نمی باشد",
                'icon': 'error',
                'confirmButtonColor': '#3085d6',
                'confirmButtonText': 'باشه ممنون'
            })
    else:
        return JsonResponse({
            'status' : 'not_auth',
            'title': 'اعلان',
            'text': "لطفا ابتدا وارد حساب کاربری خود شوید",
            'icon': 'error',
            'confirmButtonColor': '#3085d6',
            'confirmButtonText': 'باشه ممنون'
            })


@login_required()
def RemoveReservationHotelView(request):
    res_id = request.GET.get('res_id')
    print(res_id)
    if request.user.is_authenticated:
        data_res = Reservation_Hotel.objects.filter(id=res_id).first()
        date_hotel = Hotel.objects.filter(id=data_res.hotel.id).first()
        data_count = Count_Room_Hotel.objects.filter(hotel_name=date_hotel).first()

        if data_res is not None:
            data_res.delete()
            date_hotel.status = False
            count = data_count.count_room
            count = count + 1
            data_count.count_room = count
            data_count.save()
            date_hotel.save()
            return JsonResponse({
                'status' : 'success',
                'title': 'اعلان',
                'text': "اتاق شما با موفقیت حذف شد",
                'icon': 'success',
                'confirmButtonText': 'باشه ممنون'
            })
        else:
            return JsonResponse({
                'status' : 'not_found',
                'title': 'اعلان',
                'text': "اطلاعات وارد شده صحیح نمی باشد",
                'icon': 'error',
                'confirmButtonColor': '#3085d6',
                'confirmButtonText': 'باشه ممنون'
            })
    else:
        return JsonResponse({
            'status' : 'not_auth',
            'title': 'اعلان',
            'text': "لطفا ابتدا وارد حساب کاربری خود شوید",
            'icon': 'error',
            'confirmButtonColor': '#3085d6',
            'confirmButtonText': 'باشه ممنون'
            })

@login_required()
def RemoveReservationVillaView(request):
    res_id = request.GET.get('res_id')
    print(res_id)
    if request.user.is_authenticated:
        data_res = Reservation_Villa.objects.filter(id=res_id).first()
        date_villa = Villa.objects.filter(id=data_res.Villa.id).first()

        if data_res is not None:
            data_res.delete()
            date_villa.status = False
            date_villa.save()
            return JsonResponse({
                'status' : 'success',
                'title': 'اعلان',
                'text': "اتاق شما با موفقیت حذف شد",
                'icon': 'success',
                'confirmButtonText': 'باشه ممنون'
            })
        else:
            return JsonResponse({
                'status' : 'not_found',
                'title': 'اعلان',
                'text': "اطلاعات وارد شده صحیح نمی باشد",
                'icon': 'error',
                'confirmButtonColor': '#3085d6',
                'confirmButtonText': 'باشه ممنون'
            })
    else:
        return JsonResponse({
            'status' : 'not_auth',
            'title': 'اعلان',
            'text': "لطفا ابتدا وارد حساب کاربری خود شوید",
            'icon': 'error',
            'confirmButtonColor': '#3085d6',
            'confirmButtonText': 'باشه ممنون'
            })