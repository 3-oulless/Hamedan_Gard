from django.shortcuts import render,redirect
from django.views import View
from .forms import LoginWithPasswordForm,SendOtpCodeForm,VerifyPhoneForm,RegisterForm
from django.contrib.auth import login,authenticate,logout
from .models import User,OTPCode,Profile
from .OTP_Code.create_code import Otp_Digit
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from Reservation_Model.models import Reservation_Hotel,Reservation_Villa

register_info = {}

class SendOtpCode(View):

    def get(self,request):
        send_otp = SendOtpCodeForm()
        context = {
            'form':send_otp
        }
        return render(request,'Account/send_otp.html',context)
    
    def post(self,request):

        send_otp = SendOtpCodeForm(request.POST or None)

        if send_otp.is_valid():
            register_info['phone'] = send_otp.cleaned_data.get('phone')
            
            verify_code = Otp_Digit()
            # print(user_id)
            code_phone,status = OTPCode.objects.get_or_create(user=register_info['phone'],code=verify_code)
            #send sms modul
            return redirect('Account_Model:verify_otp')

        context = {
            'form':send_otp
        }
        return render(request,'Account/send_otp.html',context)


class VerifyOtpCode(View):

    def get(self,request):
        verify_otp = VerifyPhoneForm()
        context = {
            'form':verify_otp
        }
        return render(request,'Account/verify_otp_code.html',context)        

    def post(self,request):
        verify_otp = VerifyPhoneForm(request.POST or None)

        if verify_otp.is_valid():
            code = verify_otp.cleaned_data.get('code')

            otp_code = OTPCode.objects.filter(code__iexact=code,user=int(register_info['phone'])).first()
            if otp_code:
                otp_code.delete()
                return redirect('Account_Model:register')
            
        context = {
            'form':verify_otp
        }
        return render(request,'Account/verify_otp_code.html',context)

class Register(View):
    def get(self,request):
        register_form = RegisterForm()
        context = {'form':register_form}
        return render(request,'Account/register.html',context)
    
    def post(self,request):
        register_form = RegisterForm(request.POST or None)

        if register_form.is_valid():
            email = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get('password')
            first_name = register_form.cleaned_data.get('first_name')
            last_name = register_form.cleaned_data.get('last_name')


            try:
                user = User.objects.create(first_name=first_name,last_name=last_name,phone=int(register_info['phone']),email=email)
                user.set_password(password)
                user.save()
                register_info.clear()
                return redirect('Home_Model:home')
            except:
                register_info.clear()
                return redirect('Account:send_otp')


        context = {'form':register_form}
        return render(request,'Account/register.html',context)




class Login(View):

    def get(self,request):
        login_form = LoginWithPasswordForm()
        context = {
            'form':login_form
        }
        return render(request,'Account/login.html',context)
    
    def post(self,request):
        login_form = LoginWithPasswordForm(request.POST or None)        
        print(login_form)
        if login_form.is_valid():
            phone = login_form.cleaned_data.get('phone')
            password = login_form.cleaned_data.get('password')

            user = authenticate(request,phone=phone,password=password)
            if user:
                login(request,user)
                print(user)
                return redirect('Home_Model:home')

        context = {
            'form':login_form
        }
        return render(request,'Account/login.html',context)


class ProfileView(View):

    @method_decorator(login_required(login_url='/account/login/'))
    def get(self, request):
        user_id = request.user.id

        context = {
            'prof_data' : Profile.objects.filter(user_id=user_id).first(),
            'res_villa_data' : Reservation_Villa.objects.filter(user_id=user_id),
            'res_hotel_data' : Reservation_Hotel.objects.filter(user_id=user_id),
        }

        return render(request,'profile.html',context)

