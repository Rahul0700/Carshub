from django.forms import ModelForm
from accounts.models import customer,sales,inventory,accessories

class Customerform(ModelForm):
    class Meta:
        fields = ("name","contact","address")
        model = customer
class newsaleform(ModelForm):
    class Meta:
        fields = ("date","model","price_sold","car_id","emp_id","cus_id","discount","reg_fees",
        "reg_number","price_sold")
        model = sales

class add_inventory(ModelForm):
    class Meta:
        fields = ("model","built_year","is_petrol","is_testdrive","is_sold","red","blue","black",
        "price")
        model = inventory

class add_accessory(ModelForm):
    class Meta:
        fields = ( "spoiler","bumper","car_cover","car_mat")
        model = accessories
