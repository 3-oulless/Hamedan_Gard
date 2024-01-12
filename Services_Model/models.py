from django.db import models
from django.utils.text import slugify
import os
import random
import datetime

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    BASE_LIST = '0123456789abcdefghijklmnopqrstuvwxyz'
    new_name = ''.join(random.choices(BASE_LIST, k=10))
    name,ext = get_filename_ext(filename)
    x = datetime.datetime.now()
    final_name = f"services/{new_name}{ext}"
    return f"Media/{final_name}"

class Gallery_Hotel_Picture(models.Model):
    hotel_type = models.CharField(max_length=255,verbose_name="نوع اتاق")
    image_hotel = models.ImageField(upload_to=upload_image_path,verbose_name="تصویر گالری")

    def __str__(self):
        return self.hotel_type

class Option(models.Model):
    title = models.CharField(max_length=500,verbose_name="امکانات")

    def __str__(self):
        return self.title
    

class Restaurants_Type(models.Model):
    name = models.CharField(max_length=500,verbose_name="اسم")

    def __str__(self):
        return self.name

class City(models.Model):
    title_fa = models.CharField(max_length=255,verbose_name="نام")
    title_en = models.CharField(max_length=255,verbose_name="نام در url")

    def __str__(self):
        return self.title_fa

class Tourism(models.Model):

    name = models.CharField(max_length=500,verbose_name='اسم')
    city_name = models.ForeignKey(City,on_delete=models.DO_NOTHING,verbose_name="شهر")
    address = models.TextField(verbose_name="آدرس")
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to=upload_image_path, verbose_name="تصویر")

    def __str__(self):
        return self.name

class Hotel(models.Model):

    name = models.CharField(max_length=500,verbose_name="اسم")
    name_en = models.CharField(max_length=500,verbose_name="اسم انگلیسی",null=True, blank=True)
    address = models.TextField(verbose_name="آدرس")
    option = models.ManyToManyField(Option, verbose_name="امکانات")
    bed = models.IntegerField(verbose_name="تعداد تخت",blank=True,null=True)
    floor = models.IntegerField(verbose_name="طبقه",blank=True,null=True)
    room = models.IntegerField(verbose_name="اتاق",blank=True,null=True)
    description = models.TextField(verbose_name="توضیحات")
    tourist_places = models.ManyToManyField(Tourism,verbose_name="مکان توریستی") #جاذبه های نزدیک به هتل
    gallery = models.ManyToManyField(Gallery_Hotel_Picture,verbose_name="تصاویر بیشتر")
    image = models.ImageField(upload_to=upload_image_path,verbose_name="تصویر")
    price = models.BigIntegerField(verbose_name="قیمت",blank=True,null=True)
    status = models.BooleanField(default=False,verbose_name="رزرو شده/نشده",null=True,blank=True)


    def __str__(self):
        return self.name

class Count_Room_Hotel(models.Model):
    hotel_name = models.ForeignKey(Hotel,on_delete=models.DO_NOTHING,verbose_name="هتل")
    count_room = models.IntegerField(verbose_name="تعداد اتاق")

    def __str__(self):
        return self.hotel_name.name    

class Villa(models.Model):

    name = models.CharField(max_length=500,verbose_name="اسم")
    city_name = models.ForeignKey(City,on_delete=models.DO_NOTHING,verbose_name="شهر")
    address = models.TextField(verbose_name="آدرس")
    option = models.ManyToManyField(Option, verbose_name="امکانات")
    description = models.TextField(verbose_name="توضیحات")
    tourist_places = models.ManyToManyField(Tourism,verbose_name="مکان توریستی") #جاذبه های نزدیک به هتل
    image = models.ImageField(upload_to=upload_image_path,verbose_name="تصویر")
    price = models.BigIntegerField(verbose_name="اجاره",null=True,blank=True)
    status = models.BooleanField(default=False,verbose_name="رزرو شده/نشده",null=True,blank=True)
    
    def __str__(self):
        return self.name

class Restaurants(models.Model):

    name = models.CharField(max_length=500,verbose_name="اسم")
    address = models.TextField(verbose_name="آدرس")
    option = models.ManyToManyField(Option, verbose_name="امکانات")
    type_res = models.ManyToManyField(Restaurants_Type, verbose_name="نوع رستوران")
    tourist_places = models.ManyToManyField(Tourism,verbose_name="مکان توریستی",blank=True)
    image = models.ImageField(upload_to=upload_image_path,verbose_name="تصویر")

    def __str__(self):
        return self.name

class Public_Parking(models.Model):

    name = models.CharField(max_length=500,verbose_name="اسم")
    address = models.TextField(verbose_name="آدرس")
    tourist_places = models.ManyToManyField(Tourism,verbose_name="مکان توریستی") #جاذبه های نزدیک به هتل
    image = models.ImageField(upload_to=upload_image_path,verbose_name="تصویر",blank=True,null=True)

    def __str__(self):
        return self.name


class Gallery_Villa_Picture(models.Model):
    image = models.ImageField(upload_to=upload_image_path,verbose_name="تصویر گالری")
    villa_type = models.ForeignKey(Villa,on_delete=models.DO_NOTHING,verbose_name="ویلا")

    def __str__(self):
        return self.villa_type.name
    

    
