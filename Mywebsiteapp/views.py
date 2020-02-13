from django.shortcuts import render, redirect
from django.http import HttpResponse
from Mywebsiteapp.form import Categoryform, Productform, Userform, Cartform
from Mywebsiteapp.models import Category, Product, User, Cart


# Create your views here.


def index(request):
    category = Category.objects.all()

    cat = request.GET.get('category')
    if cat is not None:
        product = Product.objects.filter(Cname_id=cat)
        return render(request, 'index.html', {"catlist": category, "product": product})
    else:
        product = Product.objects.all()
        return render(request, 'index.html', {"catlist": category, "product": product})


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
    product = Productform(request.POST)
    product.save()
    return HttpResponse('<h3>success</h3>')


def adduser(request):
    user = Userform
    return render(request, 'adduser.html', {'form': user})


def saveuser(request):
    user = Userform(request.POST, request.FILES)
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


def cart(request):
    id = request.GET.get('pro_id')
    pro_id = Product.objects.get(id=id)
    email = request.session.get('Username')
    ul = User.objects.get(Email=email)
    if email is not None:
        c = Cart(pro_id, ul)
        cf = Cartform(instance=c)
        cf.save()
        return render(request, 'cart.html')
    else:
        return render(request, 'login.html')
