from django.shortcuts import render
from register.models import Student
from register.forms import StudentForm
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from register.serializers import studentSerializer


# Create your views here.   

def form_view(request):
    print("hello")
    form = StudentForm()

    if request.method =='POST':
        print(request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            print("valid succesfully")
            form.save()
        else:
            print ("vaild unsuccessfull",form.errors)
        return redirect('/mark')
        
    return render(request,'star/Home.html',{'form':form})

def register_detail_view(request):
    obj = Student.objects.all()
    # obj = Student.objects.filter(Age=16,Gender='M')
    print(obj)
    # it is for single id datas like row display only for used context {single object}
    # context = {
    #    'Application_No':obj.Application_No,
    #    'Name':obj.Name,
    #    'DOB':obj.DOB,
    #    'Age':obj.Age,
    #    'Gender':obj.Gender,
    #    'Mobile_Number':obj.Mobile_Number,
    #    'Address':obj.Address,
    # }
    return render(request,'register/detail.html',{'all':obj})


class studentList(APIView):
    def get(self,respect):
        students1= Student.objects.all()
        serializer=studentSerializer(students1,many= True)
        return Response(serializer.data)

def post(self):
    pass