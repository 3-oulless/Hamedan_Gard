import datetime
import os
import random
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver

import re



# create by matin

def normalize_mobile(phone):
        
    regex = r"\w{2,4}\w{5}\w{1,2}"
    phone_number = str(phone)
    normal_phone = re.search(regex,phone_number)
    phone = normal_phone.group() 
    return int(phone)




def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    BASE_LIST = '0123456789abcdefghijklmnopqrstuvwxyz'
    new_name = ''.join(random.choices(BASE_LIST, k=10))
    name,ext = get_filename_ext(filename)
    x = datetime.datetime.now()
    final_name = f"Profile/{new_name}{ext}"
    return f"Media/{final_name}"



class UserManager(BaseUserManager):

    def create_user(self,phone,first_name=None,last_name=None,email=None,password=None,**extra_fields):
        if not phone:
            raise ValueError("شماره تلفن را وارد کنید")
        
        phone = normalize_mobile(phone)
        email = self.normalize_email(email)
        user = self.model(phone=phone,email=email,first_name=first_name,last_name=last_name,**extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self,phone,first_name=None,last_name=None,email=None,password=None,**extra_fields):
         
        user = self.create_user(phone,password=password,email=email,first_name=first_name,last_name=last_name,**extra_fields)

        user.is_superuser = True
        user.is_staff = True
        user.is_active = True

        user.save(using=self._db)
        return user



class User(AbstractBaseUser,PermissionsMixin):
    phone = models.BigIntegerField(unique=True)
    email = models.EmailField(max_length=255,unique=False,blank=True,null=True)
    first_name = models.CharField(max_length=255,verbose_name="نام",blank=True,null=True)
    last_name = models.CharField(max_length=255,verbose_name="نام خانوادگی",blank=True,null=True)
    
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "phone"

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return f'{self.phone}'



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name="کاربر")
    image = models.ImageField(upload_to=upload_image_path,blank=True,null=True,verbose_name="پروفایل")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True,verbose_name="آپدیت")

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f'{self.user.first_name} {self.user.last_name}'
        else:
            return f'{self.user.phone}'

@receiver(post_save,sender=User)
def save_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


class OTPCode(models.Model):

    user = models.BigIntegerField(verbose_name="کاربر")
    code = models.IntegerField(verbose_name="کد تایید")

    def __str__(self):
        return f'{self.user} _ {self.code}'

class VisitCount(models.Model):
    ip = models.CharField(max_length=255,verbose_name="آی پی")

    def __str__(self):
        return self.ip