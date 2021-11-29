from django.shortcuts import render,redirect
from .models import Student
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'base.html')

def student(request):
    if request.method == 'POST':
        data = request.POST
        frist_name = data['frist_name']
        last_name = data['last_name']
        email = data['email']
        obj = Student.objects.create(frist_name=frist_name,last_name=last_name,email=email)
        if obj:
            return redirect('/student')
        else:
            return HttpResponse("Strudent not created :(")
    else:
        students = Student.objects.all()
        context = {
            'students':students
        }
    return render(request,'student.html',context)

def update_student(request,id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.frist_name = request.POST['frist_name']
        student.last_name = request.POST['last_name']
        student.email = request.POST['email']
        student.save()
        return redirect('/student')
    else:
        context = {
            'student':student
        }
        return  render(request,'update_student.html',context)

def delete_student(request,id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
          student.delete()
          return redirect('/student')
    else:
          context = {
              'student':student
          }
          return render(request,'delete_student.html',context)


        

