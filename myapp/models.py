from itertools import product
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime
# Create your models here.

class Area(models.Model):
    '''
    class for area in the app
    '''
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=250)
    #admin = models.OneToOneField(User,on_delete=models.CASCADE)

    def create_area(self):
        self.save()

    def delete_area(self):
        self.delete()
        
    def __str__(self):
         return self.name
  
class Profile(models.Model):
    '''
    class for user profiles
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    id_number = models.IntegerField(blank=True,null=True)
    profile_pic = CloudinaryField('image')
    user_email = models.EmailField()
    user_bio = models.TextField(blank=True)
    area = models.ForeignKey(Area,on_delete=models.CASCADE,blank=True,null=True)

    
    def __str__(self):
        return f'{self.user.username} profile'
    @receiver(post_save,sender=User) 
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save,sender=User) 
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()
        

class Seller(models.Model):
    '''
    Model for seller profile
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image')
    #product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    seller_email = models.EmailField()
    business_number = models.IntegerField()
    seller_bio = models.TextField(blank=True)
    area = models.ForeignKey(Area,on_delete=models.CASCADE,blank=True,null=True)
      
    def __str__(self):
        return f'{self.user.username} seller'
    
class Product(models.Model):
    '''
    Model for products class
    '''
    product_name = models.CharField(max_length=40)
    product_pic = CloudinaryField('image')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    #area = models.ForeignKey(Area,on_delete=models.CASCADE)
    product_description = models.CharField(max_length=255)
    price = models.IntegerField()
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE,blank=True,null=True)
    area = models.ForeignKey(Area,on_delete=models.CASCADE,blank=True,null=True)
    
    def __str__(self):
        return self.product_name

    def create_product(self):
        self.save()

    def delete_product(self):
        self.delete()
        
    def update_product(self):
        self.save()

    @classmethod
    def search_product(cls,search_term):
        product = Product.objects.get(product_name__icontains=search_term)
        return product
    
class Message(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    