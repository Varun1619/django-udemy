from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')
# We are importing the fields 'username','email','password' From the User Module as thay are already INBUILT

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
#Here we are asking from the models that we created in the models.py file .