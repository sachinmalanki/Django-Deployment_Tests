from django import forms
from basic_app.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    #portfolio = forms.URLField()
    #picture = forms.ImageField()

    class Meta():
        model = User
        fields = ('username','email','password')
        #exclude = ('user',)


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','portfolio_pic',)
