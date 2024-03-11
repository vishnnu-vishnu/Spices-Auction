from django.shortcuts import render,redirect
from django.contrib import messages

# from django.views.generic import CreateView,FormView,ListView,UpdateView,DetailView,TemplateView,View
# from django.shortcuts import render,redirect
# from django.urls import reverse_lazy,reverse
# from django.contrib import messages
# from django.contrib.auth import authenticate,login,logout
# from django.utils.decorators import method_decorator

# from adminapi.forms import RegistrationForm,LoginForm
from adminapi.models import Spice,Seller

def sellerlogin(request):
    return render(request,"sellerlogin.html")


def save_seller(request):
    if request.method=="POST":
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
        username=request.POST.get('username')
        obj=Seller(phone=mobile,email_address=email,password=password,username=username)
        obj.save()
        return redirect(sellerlogin)
    


def login_seller(request):
    if request.method == "POST":
        em = request.POST.get('username')
        pwd = request.POST.get('password')
        messages.success(request, "Login succesfully...!!")
        if Seller.objects.filter(username=em,password=pwd).exists():
                request.session['username']=em
                request.session['password']=pwd
                return redirect(sellerlogin)
        else:
            return redirect(sellerlogin)
    else:
        return redirect(sellerlogin)
    

def logoutseller(request):
    del request.session['username']
    del request.session['password']
    return redirect(sellerlogin)