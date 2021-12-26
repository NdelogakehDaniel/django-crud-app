from django.urls import path
from . import views as v

urlpatterns = [
    path('',v.student_form,name="student_insert"), #route to view student form and store it 
    path('<int:id>/',v.student_form,name="student_update"), #route to update a student
    path('list/',v.student_list,name="student_list") , #get method to list all students
    path('delete/<int:id>/',v.student_delete,name='student_delete')
    
]