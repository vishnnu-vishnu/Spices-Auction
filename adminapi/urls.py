from django.urls import path
from adminapi import views
urlpatterns=[
    path("seller_login/",views.sellerlogin,name="seller_logon"),
    path("save_seller/",views.save_seller,name="save_seller"),
    path("login_seller/",views.login_seller,name="login_seller"),


    

]