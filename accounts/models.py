from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.contrib.auth.models import User
# Create your models here.
class inventory(models.Model):
    car_id = models.CharField(max_length = 6)
    model = models.CharField(max_length = 20 )
    built_year = models.PositiveSmallIntegerField()
    is_petrol = models.BooleanField()
    is_diesel = models.BooleanField()
    is_testdrive = models.BooleanField()
    is_sold = models.BooleanField()
    price = models.PositiveBigIntegerField()


class employee(models.Model):
    emp_id = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length = 40)
    contact = models.CharField(max_length=10,validators=[MinLengthValidator(10)])
    car_id = models.ForeignKey(inventory, on_delete = models.CASCADE)
    is_manager = models.BooleanField(default = False)

class employee_performance(models.Model):
    emp_id = models.OneToOneField(employee,on_delete=models.CASCADE)
    month_sales = models.PositiveBigIntegerField()
    target = models.PositiveBigIntegerField()
    commission = models.PositiveBigIntegerField()



class customer(models.Model):
    cus_id  = models.CharField(max_length = 6)
    name    = models.CharField(max_length = 50)
    contact = models.CharField(max_length=10,validators=[MinLengthValidator(10)])
    address = models.CharField( max_length = 250)


class sales(models.Model):
    sale_id = models.CharField(max_length = 6)
    date = models.DateField()
    model = models.CharField(max_length = 10)
    price_sold = models.PositiveBigIntegerField()
    car_id = models.ForeignKey(inventory,on_delete = models.CASCADE)
    emp_id = models.ForeignKey(employee,on_delete = models. CASCADE)
    cus_id = models.ForeignKey(customer,on_delete = models.CASCADE)
