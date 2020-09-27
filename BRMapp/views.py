from django.shortcuts import render
from BRMapp.forms import NewProductForm,SearchForm
from BRMapp import models
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Subquery
from .models import Product


def userLogin(request):
        data={}
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                request.session['username']=username
                return HttpResponseRedirect('/BRMapp/view-products/')
            else:
                data['error']="Username or Password incorrect"
                res=render(request,'BRMapp/user_login.html',data)
                return res
        else:
            return render(request,'BRMapp/user_login.html',data)
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/BRMapp/login/')

@login_required(login_url="/BRMapp/login/")
def searchProduct(request):
        form=SearchForm()
        res=render(request,'BRMapp/search_product.html',{'form':form})
        return res
@login_required(login_url="/BRMapp/login/")
def search(request):
        form=SearchForm(request.POST)
        products=models.Product.objects.filter(title__startswith=form.data['title'])
        #products=models.Product.objects.filter(company__startswith=form.data['company'])
        #products=models.Product.objects.filter(distributer__startswith=form.data['distributer'])
        #products=models.Product.objects.filter(title=form.data['title'])
        res=render(request,'BRMapp/search_product.html',{'form':form,'products':products})
        return res
@login_required(login_url="/BRMapp/login/")
def deleteProduct(request):
        productid=request.GET['productid']
        product=models.Product.objects.filter(id=productid)
        product.delete()
        return HttpResponseRedirect('BRMapp/view-products')
@login_required(login_url="/BRMapp/login/")
def editProduct(request):
        product=models.Product.objects.get(id=request.GET['productid'])
        fields={'title':product.title,'price':product.price,'company':product.company,'distributer':product.distributer}
        form=NewProductForm(initial=fields)
        res=render(request,"BRMapp/edit_product.html",{'form':form,'product':product})
        return res
@login_required(login_url="/BRMapp/login/")
def edit(request):
    if request.method=='POST':
        form=NewProductForm(request.POST)
        product=models.Product()
        product.id=request.POST['productid']
        product.title=form.data['title']
        product.price=form.data['price']
        product.company=form.data['company']
        product.distributer=form.data['distributer']
        product.save()
        return HttpResponseRedirect('BRMapp/view-products')
@login_required(login_url="/BRMapp/login/")
def viewProducts(request):
    products=models.Product.objects.all()
    username=request.session['username']
    res=render(request,'BRMapp/view_product.html',{'products':products,'username':username})
    return res

@login_required(login_url="/BRMapp/login/")
def NewProduct(request):
    form=NewProductForm()
    res=render(request,'BRMapp/new_product.html',{'form':form})
    return res
@login_required(login_url="/BRMapp/login/")
def add(request):
    if request.method=='POST':
        form=NewProductForm(request.POST)
        product=models.Product()
        product.title=form.data['title']
        product.price=form.data['price']
        product.company=form.data['company']
        product.distributer=form.data['distributer']
        product.save()
        s="Record Stored<br><a href='/BRMapp/view-products'/>View all products</a>"
        return HttpResponse(s)
