from django.db import models


# Field here is like software engineering , networking etc
class Field(models.Model):
    title=models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class Student(models.Model):
    name=models.CharField(max_length=100)
    email = models.EmailField(max_length=30,unique=True)
    gender = models.CharField(max_length=30)
    age = models.IntegerField()
    field=models.ForeignKey(Field,on_delete=models.CASCADE)
