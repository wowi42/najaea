from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    
class Result(models.Model):
    employee = models.ForeignKey(Employee)
    created_at = models.DateTimeField('date created')
    mark = models.IntegerField(default=0)
