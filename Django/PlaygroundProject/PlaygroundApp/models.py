# from sys import last_type
from django.db import models

# Create your models here.
class Employees(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=80)
    age = models.IntegerField()

    def _str_(self):
        return self.name