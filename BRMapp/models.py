from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField(max_length=100)
    company=models.CharField(max_length=100)
    distributer=models.CharField(max_length=100)

class BRMuser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE);
    nickname=models.CharField(max_length=20,null=False);
