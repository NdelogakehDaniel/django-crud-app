from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student



#get request to get list of students
def student_list(request):
    context = {'student_list':Student.objects.all()}
    return render(request,'student_list.html',context)

# Post request to store new request
def student_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = StudentForm()
        else:
            print(id)
            student = Student.objects.get(pk=id)
            form = StudentForm(instance=student)
            
        return render(request,'base.html',{'form':form})
    else:
        if id == 0:
            form = StudentForm(request.POST)
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        else:
            return redirect('/playground/')

# delete request to delete a student
def student_delete(request,id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('/playground/list')
