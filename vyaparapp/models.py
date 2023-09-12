from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
  cust_user = models.ForeignKey(User, on_delete=models.CASCADE)
  cust_mobile = models.CharField(max_length=10, default=10)
  
  