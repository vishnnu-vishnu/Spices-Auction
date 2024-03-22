from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator,MaxValueValidator


class Seller(models.Model):
    username=models.CharField(max_length=100)
    email_address=models.EmailField()
    password=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    is_available=models.BooleanField(default=True,null=True)
    
    
class user(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email_address=models.EmailField()
    address=models.CharField(max_length=100,null=True)
    id_proof=models.FileField(null=True,upload_to="images")
    profile=models.ImageField(upload_to="images",null=True)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    is_available=models.BooleanField(default=True,null=True)

    def __str__(self):
        return self.firstname
    
    
class Spice(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.name 
    
    
class Auction(models.Model):
    spice=models.ForeignKey(Spice,on_delete=models.CASCADE)
    start_price=models.PositiveIntegerField()
    end_time=models.DateTimeField()
    winner=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    
    
class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bidder = models.ForeignKey(user, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Bid of {self.amount} by {self.bidder.username}"