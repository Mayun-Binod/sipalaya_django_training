from django.contrib import admin
from app.models import *
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','address','phone']


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'images']
