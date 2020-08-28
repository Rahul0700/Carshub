from django.contrib import admin
from .models import employee,customer,employee_performance

#Register your models here.
admin.site.register(employee)
admin.site.register(employee_performance)
