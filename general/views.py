from django.shortcuts import render
from django.shortcuts import render
from .forms import Customerform,newsaleform
from accounts.models import customer,inventory
from random import randint
# Create your views here.
def customersignup(request):
    if request.method == 'POST':
        form = Customerform(data=request.POST)
        if form.is_valid():
            upload_form = form.save(commit=False)
            integrity=False
            while(integrity==False):
                random_code = randint(1000,9999)
                code = 'CUS'+str(random_code)
                try:
                    customer.objects.get(cus_id=code)
                    integrity = False
                except :
                    integrity = True
            upload_form.customer = form
            upload_form.cus_id  = code
            upload_form.save()
    else:
        form = Customerform()
    return render(request,'general/booking_form.html',{'form':form})

def addsale(request):
    if request.method == 'POST':
        form = newsaleform(data=request.POST)
        if form.is_valid():
            upload_form = form.save(commit=False)
            integrity=False
            while(integrity==False):
                random_code = randint(1000,9999)
                code = 'SEL'+str(random_code)
                try:
                    customer.objects.get(sale_id=code)
                    integrity = False
                except :
                    integrity = True
            upload_form.sales = form
            upload_form.sale_id  = code
            upload_form.save()
    else:
        form = newsaleform()
    return render(request,'general/sale_form.html',{'form':form})

def inventory_showcase(request):
        storage = inventory.objects.raw('SELECT * FROM accounts_inventory')
        return render(request,'inventory.html',{ 'inventory': storage})
