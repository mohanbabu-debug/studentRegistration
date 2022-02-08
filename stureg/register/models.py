import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Student(models.Model):
    Application_No = models.AutoField(primary_key=True)
    Name           = models.CharField(max_length = 20)
    DOB            = models.DateField()
    Age            = models.IntegerField()
    GENDER_CHOICES = (
        ('S','Select'),
        ('F','Female'),
        ('M','Male')
    )
    Gender         = models.CharField(max_length=1, choices=GENDER_CHOICES, default = 'Select')
    Mobile_Number  = models.CharField(max_length=10)
    Address        = models.TextField()
    Register_on    = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.Name


    
   
