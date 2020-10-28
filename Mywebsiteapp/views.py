from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from Mywebsiteapp.form import Categoryform, Productform, Userform
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
import datetime


# Create your views here.


def index(request):
    email = request.session.get('Username')
    category = Category.objects.all()

    cat = request.GET.get('category')
    if cat is not None:
        product = Product.objects.filter(Cname_id=cat)

        context = {"catlist": category,
                   "product": product}
        # return render(request, 'index.html', {"catlist": category, "product": product})
    else:
        if email is not None:
            customer = User.objects.get(Email=email)
            order, created = Order.objects.get_or_create(
                customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cartItems = order['get_cart_items']
        product = Product.objects.all()
        context = {"catlist": category,
                   "product": product, "cartItems": cartItems}
    return render(request, 'index.html', context)


# def getproduct(request, CName):
#     product = Product.objects.filter(Cname_id=CName)
#     return render(request, "index.html", {"product": product})


def addcategory(request):
    cat = Categoryform
    return render(request, 'addcategory.html', {'form': cat})


def savecategory(request):
    category = Categoryform(request.POST)
    category.save()
    return HttpResponse('<h3>success</h3>')


def addproduct(request):
    product = Productform
    return render(request, 'addproduct.html', {'form': product})


def saveproduct(request):
    product = Productform(request.POST, request.FILES)
    product.save()
    return HttpResponse('<h3>success</h3>')


def adduser(request):
    user = Userform
    return render(request, 'adduser.html', {'form': user})


def saveuser(request):
    user = Userform(request.POST)
    user.save()
    return redirect('/userlist')


def categorylist(request):
    catlist = Category.objects.all()
    return render(request, 'categorylist.html', {'catlist': catlist})


def userlist(request):
    ulist = User.objects.all()
    return render(request, 'userlist.html', {'ulist': ulist})


def productlist(request):
    plist = Product.objects.all()
    return render(request, 'productlist.html', {'plist': plist})


def deleteuser(request):
    Email = request.GET.get('Email')
    deleteuser = User.objects.get(Email=Email)
    deleteuser.delete()
    return redirect('/userlist')


def deleteproduct(request, id):
    # id = request.GET.get('id')
    delproduct = Product.objects.get(id=id)
    delproduct.delete()
    return redirect('/productlist')


def deletecategory(request, CName):
    # CName = request.GET.get('CName')
    delcategory = Category.objects.get(CName=CName)
    delcategory.delete()
    return redirect('/categorylist')


def editcategory(request, CName):
    editcat = Category.objects.get(CName=CName)
    return redirect('/categorylist')


def editproduct(request, id):
    id = Product.objects.get(id=id)
    form = Productform(instance=id)
    # updatepro.save()
    return render(request, 'editproduct.html', {'form': form, 'id': id})


def updateproduct(request, id):
    product = Product.objects.get(id=id)
    updatepro = Productform(request.POST, instance=product)
    if updatepro.is_valid():
        updatepro.save()
        return redirect('/productlist')
    return redirect('/productlist')


def login(request):
    return render(request, "login.html")


def loginuser(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    if email == 'admin@gmail.com' and password == 'admin':
        request.session['Adminname'] = email
        return redirect('/home')
    else:
        try:
            ul = User.objects.get(Email=email)
            if email == ul.Email and password == ul.Password:
                request.session['Username'] = email
                return redirect('/home')
            else:
                return render(request, 'login.html', {'lm': "invalid user name or password"})
        except:
            return render(request, 'login.html', {'lm': "invalid user name or password"})


def logout(request):
    try:
        ls = list(request.session.keys())
        for i in ls:
            del request.session[i]

    except KeyError:
        pass
    return redirect('/home')


def add_to_cart(request):

    email = request.session.get('Username')
    if email is not None:
        p_id = request.GET.get("pro_id")
        product = Product.objects.get(id=p_id)
        user = User.objects.get(Email=email)
        user_cart = Cart()
        if Cart.objects.filter(Product=product).exists():
            messages.success(request, 'Product already added in your Cart.')
            return redirect('/home')
        else:
            user_cart.Email = user
            user_cart.Product = product
            user_cart.save()
            return redirect('/home')
    else:
        return redirect('/login')


def cart(request):
    email = request.session.get('Username')
    if email is not None:
        customer = User.objects.get(Email=email)
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    # print(context)
    return render(request, 'cart.html', context)


def checkout(request):
    email = request.session.get('Username')
    if email is not None:
        customer = User.objects.get(Email=email)
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    # print(context)
    return render(request, 'checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = User.objects.get(Email=request.session.get('Username'))
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0 or action == 'delete':
        orderItem.delete()

    return JsonResponse('item was added', safe=False)


def processOrder(request):
    print('data:', request.body)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    email = request.session.get('Username')
    if email is not None:
        customer = User.objects.get(Email=email)
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        total = float(data['shippingInfo']['total'])
        print('total:', total)
        order.transaction_id = transaction_id
        if total == float(order.get_cart_total):
            order.complete = True
        order.save()

        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shippingInfo']['address'],
            city=data['shippingInfo']['city'],
            state=data['shippingInfo']['state'],
            zipcode=data['shippingInfo']['zipcode'],
        )
        print(ShippingAddress.address)
    else:
        print('User is not logged in')

    return JsonResponse('Payment Complete', safe=False)


# def cart(request):
#     id = request.GET.get("id")
#     if id is not None:
#         cartproduct = Cart.objects.get(id=id)
#         cartproduct.delete()
#         # error = 'notdeleted'
#         return HttpResponse("delete")
#         # return redirect("cart")
#         # cart(request)
#     else:
#         cartitem = Cart.objects.filter(Email=request.session.get("Username"))
#         tp = 0
#         for item in cartitem:
#             tp = tp+int(item.Product.Price)

#         return render(request, 'cart.html', {"cartitems": cartitem, "tp": tp})


# def checkoutcart(request):
#     pid = request.GET.get("data")
#     print(pid)
#     # return HttpResponse(pid)
#     return render(request, 'checkout.html')
