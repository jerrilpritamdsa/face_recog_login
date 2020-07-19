from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    description =models.CharField(max_length=100,default=' ')
    city=models.CharField(max_length=20,default="")
    phone=models.IntegerField(default=0)
    head_shot=models.ImageField(upload_to='profile_images',blank=True)
    
    
    class Meta:
        ordering = ["user"]

    def __str__(self):
        return self.user.username
    
    
class LogTimes(models.Model):
    login_time=models.DateTimeField(auto_now_add=True, null=True)
    logout_time=models.DateTimeField(auto_now_add=True, null=True)
    user=models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["user"]
        
    def __str__(self):
        return self.user.user.username
    
    
def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.get_or_create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)