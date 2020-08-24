from django.forms import ModelForm
from accounts.models import customer

class Customerform(ModelForm):
    class Meta:
        fields = ("name","contact","address")
        model = customer
