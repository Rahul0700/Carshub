from django.urls import path
from accounts import views

app_name = 'general'

urlpatterns = [
    path('employeesignup/',views.employeesignup,name='employee_sign'),
]
