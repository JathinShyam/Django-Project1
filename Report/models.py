from django.db import models

class Employee(models.Model):
    staffId= models.IntegerField()
    staffName= models.CharField(max_length=30)
    Designation= models.CharField(max_length=30)
    Salary= models.IntegerField()

    def __str__(self):
        return self.staffName
    class Meta:
        ordering=('staffName',)


