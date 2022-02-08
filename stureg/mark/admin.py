from django.contrib import admin
from .models import StudentMark

# Register your models here.
class StudentMarkAdmin(admin.ModelAdmin):
    list_display=['Application_No','Tamil','English','Maths','Science','Social']


admin.site.register(StudentMark,StudentMarkAdmin)