from .models import employee,employee_performance# DB models
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError,EmailField,ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

#employee form
class employee_form_create(UserCreationForm):
    email = EmailField(required = True)
    class Meta:
        fields = ('username','email','password1','password2')#pasword2 is more like confirm password
        model = get_user_model()#Lookup on This

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_mail(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")

        if email and User.objects.filter(email=email).exclude(username = username).exists():
            raise ValidationError(u'This Email Address already holds an account.')
        return email

#Customer form

class employeeProfileForm(ModelForm):
    class Meta:
        fields = ('contact','is_manager','blood_group',"door_no","street","city","state","pin_code")
        model = employee

class employeedetails(ModelForm):
    class Meta:
        fields = ('emp_id','target','commission')
        model = employee_performance
