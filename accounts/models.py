from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.contrib.auth.models import User
# Create your models here.

class inventory(models.Model):
    slug = models.SlugField(unique=True,null=True)
    car_id = models.CharField(max_length = 6)
    model = models.CharField(max_length = 20 )
    built_year = models.PositiveSmallIntegerField()
    is_petrol = models.BooleanField()
    is_testdrive = models.BooleanField()
    is_sold = models.BooleanField()
    price = models.PositiveBigIntegerField()
    red = models.BooleanField(default = False)
    black = models.BooleanField(default = False)
    blue = models.BooleanField(default = False)
    def __str__(self):
        return self.car_id



class employee(models.Model):
    emp_id = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length = 40)
    contact = models.CharField(max_length=10,validators=[MinLengthValidator(10)])
    is_manager = models.BooleanField(default = False)
    address = models.CharField(max_length = 250,  default="")
    door_no = models.CharField(max_length=10, default="")
    street = models.CharField(max_length=40, default="")
    city = models.CharField(max_length=40, default="")
    state = models.CharField(max_length=40,default="")
    pin_code = models.CharField(max_length=6,validators=[MinLengthValidator(6)], null=True)
    blood_group = models.CharField(max_length = 5, default="")
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
      self.address=self.door_no+", "+self.street+", "+self.city+", "+self.state+", "+self.pin_code
      super(employee, self).save(*args, **kwargs)

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

    def __str__(self):
        return self.cus_id


class sales(models.Model):
    sale_id = models.CharField(max_length = 6)
    date = models.DateField()
    model = models.CharField(max_length = 10)
    car_id = models.OneToOneField(inventory,on_delete = models.CASCADE)
    emp_id = models.ForeignKey(employee,on_delete = models. CASCADE)
    cus_id = models.ForeignKey(customer,on_delete = models.CASCADE)
    price_sold = models.PositiveBigIntegerField()
    discount = models.PositiveBigIntegerField(null=True)
    reg_fees = models.PositiveBigIntegerField(null =True)
    reg_number = models.CharField(max_length=10,default= "")
    def __str__(self):
        return self.sale_id

class accessories(models.Model):
    sale_id = models.OneToOneField(sales,on_delete = models.CASCADE)
    spoiler = models.BooleanField(default = False)
    bumper = models.BooleanField(default = False)
    car_cover = models.BooleanField(default = False)
    car_mat = models.BooleanField(default = False)
