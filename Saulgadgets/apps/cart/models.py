from django.db import models

# Create your models here.

class Payment(models.Model):
    amount = models.PositiveIntegerField()
    address = models.CharField(max_length=200)
    email =models.EmailField()
    phone_number =models.CharField( max_length=20,default=False)
    full_name =models.CharField( max_length=200, default=False)

