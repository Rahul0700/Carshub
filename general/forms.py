from django.forms import ModelForm
from accounts.models import customer,sales

class Customerform(ModelForm):
    class Meta:
        fields = ("name","contact","address")
        model = customer
class newsaleform(ModelForm):
    class Meta:
        fields = ("date","model","price_sold","car_id","emp_id","cus_id")
        model = sales
