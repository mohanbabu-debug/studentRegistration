from django.db import models
from register.models import Student


# Create your models here.
class StudentMark(models.Model):
    Application_No = models.ForeignKey(Student,default=1,verbose_name="Name",on_delete=models.SET_DEFAULT)
    Tamil          = models.IntegerField()
    English        = models.IntegerField()
    Maths          = models.IntegerField()
    Science        = models.IntegerField()
    Social         = models.IntegerField()
    
