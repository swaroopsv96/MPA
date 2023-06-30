from django.db import models

class Employee(models.Model):
    employee_name = models.CharField(max_length=255)
    employee_salary = models.IntegerField()
    employee_age = models.IntegerField()

    def __str__(self):
        return self.employee_name