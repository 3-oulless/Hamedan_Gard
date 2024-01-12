from django.db import models
from Account_Model.models import User
from Services_Model.models import Hotel,Villa

class Reservation_Hotel(models.Model):

    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name="کاربر")
    hotel = models.ForeignKey(Hotel, on_delete=models.DO_NOTHING,verbose_name="هتل")
    in_hotel = models.CharField(max_length=250,verbose_name="تاریخ رزرو")
    count = models.IntegerField(verbose_name="تعداد شب ماندگاری",null=True,blank=True)
    price = models.BigIntegerField(verbose_name="هزینه")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.hotel.name}'
    

class Reservation_Villa(models.Model):

    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name="کاربر")
    Villa = models.ForeignKey(Villa, on_delete=models.DO_NOTHING,verbose_name="ویلا")
    in_hotel = models.CharField(max_length=250,verbose_name="تاریخ رزرو")
    count = models.IntegerField(verbose_name="تعداد شب ماندگاری",null=True,blank=True)
    price = models.BigIntegerField(verbose_name="هزینه")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.Villa.name}'
