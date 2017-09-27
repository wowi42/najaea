from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Result(models.Model):
    employee = models.ForeignKey(Employee)
    created_at = models.DateTimeField('date created')
    mark = models.IntegerField(default=0)
    def __str__(self):
        return self.employee.first_name + " " + self.employee.last_name + " " + str(self.mark)
