from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    mobile=models.CharField(max_length=13,null=True,blank=True)
    last_login=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    def __str__(self):
        return self.user.username +'<-->' + self.user.first_name
    


