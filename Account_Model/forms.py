from django import forms
from .models import User,OTPCode

class SendOtpCodeForm(forms.Form):
    
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"شماره همراه"}),required=True,label="شماره همراه")

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        user = User.objects.filter(phone=phone).first()

        if user:
            raise forms.ValidationError("شماره وارد شده وجود دارد")
        return phone

class VerifyPhoneForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'کد تایید خود را وارد کنید'}),required=True,label='کد تایید')

    def clean(self):
        cleaned_data = super().clean()
        code = cleaned_data.get('code')
        verify_code = OTPCode.objects.filter(code=code).first()

        if verify_code:
            return cleaned_data
        self.add_error('code','کد وارد شده اشتباه می باشد')

class RegisterForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'پسورد'}),required=True,label="کلمه ورود")
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'تکرار پسورد'}),required=True,label="تکرار کلمه ورود")
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'ایمیل'}),required=False,label="ایمیل")
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام'}),required=True,label="نام")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام خانوادگی'}),required=True,label="نام خانوادگی")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password != re_password:
            self.add_error('password',"پسورد ها با هم تطابق ندارند")
        return cleaned_data
    

    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        user = User.objects.filter(email=email).first()

        if user:
            raise forms.ValidationError('ایمیل وارد شده موجود میباشد')
        return email
    
class LoginWithPasswordForm(forms.Form):

    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,label="شماره همراه")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','onclick':'show()'}),label="پسورد")

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get('phone')
        
        user = User.objects.filter(phone=phone).first()

        if user:
            return cleaned_data
        self.add_error('phone','شماره وارد شده موجود نمیباشد ابتدا ثبت نام کنید')