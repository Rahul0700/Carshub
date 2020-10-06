from django.shortcuts import render
from django.shortcuts import render
from .forms import Customerform,newsaleform,add_inventory,add_accessory
from accounts.models import customer,inventory,employee,sales
from random import randint
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def customersignup(request):
    flag = "Yo"
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
            messages.success(request,'Customer with CustomerID %s added'%code)
            upload_form.save()
            return HttpResponseRedirect(reverse('general:sales'))
    else:
        form = Customerform()
    return render(request,'general/booking_form.html',{'form':form,
                                                        'flag': flag})

def addsale(request):
    for_sake = "Nothing"
    current = employee.objects.get( emp_id = request.user )
    is_manager = current.is_manager
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
            car = upload_form.car_id
            storage = inventory.objects.filter(car_id = car)
            for i in storage:
                i.is_sold = True
                i.save()
            slug = code
            return HttpResponseRedirect(reverse('general:add_accessories', kwargs = {'slug':slug}))
            #sold = inventory.objects.all()
    else:
        form = newsaleform()
#Filtered showcase
    storage = inventory.objects.raw('SELECT * FROM accounts_inventory')
    if request.method =="GET":
        mod = request.GET.get("model")
        start = request.GET.get("start_year")
        end = request.GET.get("end_year")
        storage = inventory.objects.filter(model = mod)
        storage = storage.filter(built_year = start)
        if(len(storage)==0):
            search = True
            messages.warning(request,"No inventory with these attributes")
            for_sake = "Hey"

    return render(request,'general/sale_form.html',{'form':form,
                                                    'inventory': storage,
                                                    'is_manager': is_manager,
                                                    'for_sake': for_sake})

def inventory_add(request):
    if request.method == 'POST':
        #hidden = request.POST.get("hidden_unit")
        form = add_inventory(data=request.POST)
        if form.is_valid():
            upload_form = form.save(commit=False)
            integrity=False
            while(integrity==False):
                random_code = randint(1000,9999)
                code = 'CAR'+str(random_code)
                try:
                    customer.objects.get(sale_id=code)
                    integrity = False
                except :
                    integrity = True
            upload_form.sales = form
            upload_form.car_id  = code
            messages.success(request,'Car ID of Car is : %s'%code)
            upload_form.save()
            car = upload_form.car_id

    else:
        form = add_inventory()
    return render(request,'general/add_inventory.html',{'form':form})



def inventory_delete(request):
#inventory Deletion
    storage = inventory.objects.raw('SELECT * FROM accounts_inventory')
    if request.method == "POST":
        mod = request.POST.get("model")
        start = request.POST.get("start_year")
        end = request.POST.get("end_year")
        print(start)
        storage= inventory.objects.filter(built_year = start)
        print(storage)
        storage.delete()
    return render(request,'inventory.html',{'inventory': storage})

def inventory_alter(request):
    if request.method =="POST":
        id = request.POST.get("id")
        mod_update = request.POST.get("mod_update")
        storage = inventory.objects.filter(car_id = id)
        for i in storage:
            i.model = mod_update
            i.save()
    return render(request,'inventory_update.html')

def accessories(request,slug):
    if request.method == "POST":
        form = add_accessory(data = request.POST)
        print(slug)
        if form.is_valid():
            upload_form = form.save(commit = False)
            sale = sales.objects.get(sale_id=slug)
            upload_form.sale_id = sale
            upload_form.save()
    else:
        form = add_accessory()
    return render(request,'general/add_accessories.html',{'form':form})
