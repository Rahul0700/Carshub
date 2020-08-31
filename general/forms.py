from django.forms import ModelForm
from accounts.models import customer,sales,inventory

class Customerform(ModelForm):
    class Meta:
        fields = ("name","contact","address")
        model = customer
class newsaleform(ModelForm):
    class Meta:
        fields = ("date","model","price_sold","car_id","emp_id","cus_id")
        model = sales

class add_inventory(ModelForm):
    class Meta:
        fields = ("model","built_year","built_year","is_petrol","is_diesel","is_testdrive","is_sold","price")
        model = inventory
