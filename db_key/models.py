
from django.db import models

# Create your models here.

class course(models.Model):
    course_name = models.CharField(max_length=255)
    fee = models.IntegerField()

    def __str__(Self):
        return Self.course_name

class student(models.Model):
    course = models.ForeignKey(course,on_delete = models.CASCADE,null = True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.IntegerField()
    join_date = models.DateField() 


    def __str__(Self):
        return Self.name

