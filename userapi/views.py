from django.shortcuts import render,redirect
from adminapi.models import user

# Create your views here.



def loginpage(request):
    return render (request,"loginpage.html")


def saveuser(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        mobile=request.POST.get('fname')
        password=request.POST.get('password')
        username=request.POST.get('username')
        doc=request.FILES['doc']
        obj=user(firstname=fname,lastname=lname,phone=mobile,email_address=email,id_proof=doc,password=password,username=username)
        obj.save()
        return redirect(loginpage)

