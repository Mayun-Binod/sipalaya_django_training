from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.IntegerField()

class Detail(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    images=models.ImageField(upload_to='media/')
    

