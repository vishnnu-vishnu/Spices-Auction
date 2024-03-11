from django.urls import path
from userapi import views

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('',views.loginpage,name="loginpage"),
    path('saveuser/',views.saveuser,name="saveuser"),
    path('login_user/',views.login_user,name="login_user"),
    path('logout_user/',views.logoutuser,name="logout_user")


]