from django.urls import path
from general import views

app_name = 'general'

urlpatterns = [
    path('customerdetails/',views.customersignup,name='booking'),
    path('newsale/',views.addsale,name="sales"),
    path('inventory/',views.inventory_showcase, name = "inventory"),
]
