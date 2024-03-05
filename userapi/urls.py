from django.urls import path
from userapi import views

urlpatterns = [
    path('loginpage/',views.loginpage,name="loginpage"),
    path('saveuser/',views.saveuser,name="saveuser"),

]