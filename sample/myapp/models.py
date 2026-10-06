from django.db import models
from django.contrib import admin
class vehicle(models.Model):
    Name=models.CharField(max_length=15)
    Mobile=models.IntegerField()
    Reg_no=models.CharField(primary_key=True)
    Father_name=models.TextField()
    Alt_num=models.IntegerField()
    Address=models.TextField()
    Vehicle_Type=models.TextField()
class vehicleAdmin(admin.ModelAdmin):
    list_display=["Name",'Alt_num','Reg_no','Father_name','Mobile','Address','Vehicle_Type']

