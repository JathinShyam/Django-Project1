from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display= ('staffId', 'staffName', 'Designation', 'Salary')

admin.site.register(Employee, EmployeeAdmin)
