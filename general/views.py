from django.shortcuts import render
from django.shortcuts import render
from .forms import Customerform
from accounts.models import customer
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
            upload_form.booking = booking
            upload_form.cus_id  = code
            upload_form.save()
    else:
        form = Customerform()
    return render(request,'general/booking_form.html',{'form':form})
