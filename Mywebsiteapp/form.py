from django import forms
from Mywebsiteapp.models import Category, User, Product

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
        fields='__all__'