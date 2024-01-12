from django.db import models

class ContactUs(models.Model):

    full_name = models.CharField(max_length=500,verbose_name="نام و نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل")
    subject = models.CharField(max_length=500,verbose_name="عنوان")
    comment = models.TextField(verbose_name="پیام")

    def __str__(self):
        return self.full_name