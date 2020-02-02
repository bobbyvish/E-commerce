"""MYwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index', views.index),
    path('addcategory', views.addcategory),
    path('savecategory', views.savecategory),
    path('adduser', views.adduser),
    path('saveuser', views.saveuser),
    path('addproduct', views.addproduct),
    path('saveproduct', views.saveproduct),
    path('categorylist', views.categorylist),
    path('userlist', views.userlist),
    path('productlist', views.productlist),
    path('deleteuser', views.deleteuser),
    path('deleteproduct/<int:id>', views.deleteproduct),
    path('deletecategory/<str:CName>', views.deletecategory),
    path('editcategory/<str:CName>', views.editcategory)
]
