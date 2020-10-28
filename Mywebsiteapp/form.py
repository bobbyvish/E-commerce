from django import forms
from Mywebsiteapp.models import *


class Categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class Productform(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


# class Cartform(forms.ModelForm):
#     class Meta:
#         model = Cart
#         fields = '__all__'
