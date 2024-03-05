from django.shortcuts import render
from django.views.generic import CreateView,FormView,ListView,UpdateView,DetailView,TemplateView,View
from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

from adminapi.forms import RegistrationForm,LoginForm
from adminapi.models import admin,Spice



class SignUpView(View):

    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"registration succesfully completed")
            return redirect("signin")
        else:
            messages.error(request,"failed to created account")
            return render(request,"register.html",{"form":form})
        


class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login success")
                return redirect("index")
            else:
                messages.error(request,"invalid credentials!!!!")
                return render(request,"login.html",{"form":form})

            
class IndexView(TemplateView):
    template_name="index.html"
    
    
class SpicesListView(ListView):
    model=Spice
    template_name="item_list.html"
    context_object_name="spices"