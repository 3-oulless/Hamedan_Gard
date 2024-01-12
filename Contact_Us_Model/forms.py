from django import forms

class ContactUserForm(forms.Form):

    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control shadow','placeholder':"نام شما"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control shadow','placeholder':"ایمیل"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control shadow','placeholder':"عنوان"}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control shadow','placeholder':"پیام",'rows':"5"}))
    