from django.forms import ModelForm
from .models import UserData
from django import forms


class UserDataForm(ModelForm):
    phone = forms.CharField(max_length=20, required=False)
    email = forms.CharField(max_length=20, required=False)

    class Meta:
        model = UserData
        fields = ['name', 'sure_name', 'pesel']