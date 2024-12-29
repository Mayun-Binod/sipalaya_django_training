from django.db import models
from django.core.validators import MaxValueValidator,MinLengthValidator,MinValueValidator
from datetime import datetime
import uuid
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200,default="admin")
    age=models.IntegerField(default=24)
    email=models.EmailField(unique=True)
    message=models.TextField(blank=True)
    dob=models.DateField(null=True,blank=True)

class Student(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    email=models.EmailField()
    message=models.TextField()
    dob=models.DateField(null=True)
    
   
gender_field=(
    ('male',"maaaale"),
    ('female','female'),
    ('other','other')
) 
subject_field=(
    ('nepali',"nepali"),
    ("english","english"),
    ("social","social")
)
class Detail(models.Model):
    Iswork=models.BooleanField(default=True,verbose_name="please check in ")
    name=models.CharField(max_length=200,default="sujan")
    desc=models.TextField(blank=True)
    age=models.IntegerField(null=True,validators=[MaxValueValidator(100),MinValueValidator(0)])
    # age=models.SmallIntegerField()
    # age=models.PositiveIntegerField()
    # price=models.BigIntegerField()
    price=models.DecimalField(max_digits=8,decimal_places=2,default=0)
    email=models.EmailField(unique=True,null=True)
    # image=models.ImageField(upload_to="image")
    # file=models.FileField(upload_to="file")
    # date=models.DateField(default=datetime.now())
    # date1=models.DateTimeField(default=datetime.now())
    
    # created_date=models.DateTimeField(auto_now_add=True,null=True)
    # update_date=models.DateTimeField(auto_now=True)
    pk_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    gender=models.CharField(choices=gender_field,max_length=200,null=True)
    subject=MultiSelectField(choices=subject_field,default="social") #pip install django-multiselectfield
    # pip install django-phonenumber-field
    # pip install phonenumbers
    phone=PhoneNumberField(blank=True,region="NP")
    

class Interest(models.Model):
    title=models.CharField(max_length=200)
    def __str__(self):
        return self.title
    
class City(models.Model):
    title=models.CharField(max_length=200)
    def __str__(self):
        return self.title
    
class Person(models.Model):
    name=models.CharField(max_length=200)
    interest=models.ManyToManyField(Interest)
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    person=models.OneToOneField(Person, on_delete=models.CASCADE)
    city=models.ForeignKey(City, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.person.name
    
    
    
    
    
    
    
    
    
    
  
    
