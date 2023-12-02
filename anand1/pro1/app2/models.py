from django.db import models

# Create your models here.
class employee(models.Model):
    empid=models.IntegerField()
    empname=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    salary=models.IntegerField()
    # def __str__(self):
    #     return self.empid