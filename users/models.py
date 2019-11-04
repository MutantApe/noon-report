from django.db import models
import datetime
from django.utils import timezone
'''class User(models.model):
    name = models.CharField(max_length=50,null=True)

    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Teacher(models.Model):
    user        =   models.OneToOneField(User,on_delete=models.CASCADE)
    name        =   models.CharField(max_length=50)
    department  =   models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name'''


class Student(models.Model):
    date    = models.DateField(("Date"))
    #user    =   models.OneToOneField(User,on_delete=models.CASCADE)
    name    =   models.CharField(max_length=50)
    #teacher =   models.ForeignKey(Teacher,null=True,on_delete=models.CASCADE,related_name='teacher_serial')
    roll    =   models.IntegerField(null=True)
    def __str__(self):
        return self.name
    class meta:
        db_table = "student_table"