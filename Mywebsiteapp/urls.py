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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('home', views.index),


    #   category
    path('addcategory', views.addcategory),
    path('savecategory', views.savecategory),
    path('categorylist', views.categorylist),
    path('deletecategory/<str:CName>', views.deletecategory),
    path('editcategory/<str:CName>', views.editcategory),

    # user
    path('adduser', views.adduser),
    path('saveuser', views.saveuser),
    path('userlist', views.userlist),
    path('deleteuser', views.deleteuser),

    # product
    path('addproduct', views.addproduct),
    path('saveproduct', views.saveproduct),
    path('productlist', views.productlist),
    path('deleteproduct/<int:id>', views.deleteproduct),
    path('editproduct/<int:id>', views.editproduct),
    path('updateproduct/<int:id>', views.updateproduct),
    # path('getproduct/<str:CName>', views.getproduct),



    path('login', views.login),
    path('loginuser', views.loginuser),
    path('logout', views.logout),

    # cart
    path('cart', views.cart),
    path('add_to_cart', views.add_to_cart),
    path('checkout', views.checkoutcart),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
