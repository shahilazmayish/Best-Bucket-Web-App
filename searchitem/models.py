from django.db import models

# Create your models here.


class Product(models.Model):
    name  = models.CharField(max_length=50)
    img   = models.ImageField(upload_to='pics')
    desc  = models.TextField()
    price = models.IntegerField()
    brand = models.CharField(max_length=20)
