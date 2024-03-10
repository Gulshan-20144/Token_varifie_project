from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Users(models.Model):
    user_id=models.AutoField(primary_key=True,unique=True)
    name=models.CharField(max_length=20)
    mobile=models.IntegerField()
    gmail=models.CharField(max_length=40,blank=True,null=True)
    age=models.DateTimeField(blank=True,null=True)

class company(models.Model):
    c_name=models.CharField(max_length=50)
    user=models.ForeignKey(Users,related_name="user_details",null=True,on_delete=models.CASCADE,)
    adminuser=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.c_name
    