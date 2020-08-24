from django.shortcuts import render
from .forms import employee_form_create,employeeProfileForm

# Create your views here.
def employeesignup(request):
    if request.method == 'POST':
        employee_form = employee_form_create(data=request.POST)
        employee_profile_form = employeeProfileForm( data = request.POST )

        if employee_form.is_valid() and employee_profile_form.is_valid():
            info_form = employee_form.save(commit=False)
            details_form = employee_profile_form.save(commit=False)
            details_form.name = info_form.username
            integrity = False
            while(integrity == False):
                random_code = randint(1000,9999)
                code = 'EMP'+ str(random_code)
                try:
                    User.objects.get(username=code)
                    integrity = False
                except:
                    integrity = True
            if integrity:
                info_form.username = code
                details_form.employee = info_form
                info_form.save()
                details_form.save()
    else :
        employee_form = employee_form_create()
        employee_profile_form = employeeProfileForm()
    return render(request,'accounts/employees.html',{'form': employee_form,
                                                  'profile_form':employee_profile_form})
