from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
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
    #id_number = models.IntegerField(blank=True,null=True)
    profile_pic = CloudinaryField('image')
    email = models.EmailField()
    bio = models.TextField(blank=True)
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
        
        
class Product(models.Model):
    