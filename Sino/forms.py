from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import customer


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class OrderForm(ModelForm):
    class Meta:
        model=customer
        fields='__all__'
