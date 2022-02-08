from django.contrib import admin
from register.models import Student


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['Name', 'DOB', 'Age', 'Gender', 'Mobile_Number', 'Address', 'Register_on' ]

admin.site.register(Student,StudentAdmin)


