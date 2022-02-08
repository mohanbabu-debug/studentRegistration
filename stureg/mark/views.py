from django.shortcuts import render

# Create your views here.
from mark.models import StudentMark
from mark.form import StudentMarkForm
from django.shortcuts import redirect


def formmark_view(request):
    print("Hello")
    form = StudentMarkForm()

    if request.method =='POST':
        print(request.POST)
        form = StudentMarkForm(request.POST)
        if form.is_valid():
            print("valid succesfully")
            form.save()
        else:
            print ("vaild unsuccessfull",form.errors)
        return redirect('/admin')
        
    return render(request,'star/House.html',{'form':form})
