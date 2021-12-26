from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ('name','email','gender','age','field')
        labels={
            'name':'User Name',
            'field': 'Field of Study'
        }
    
    # used to initialise the option field so instead of ----- it shows Select  
    def __init__(self,*args,**kwargs):
        super(StudentForm,self).__init__(*args,**kwargs)
        self.fields['field'].empty_label="Select"
        self.fields['name'].required = False