from django.urls import path
from general import views

app_name = 'general'

urlpatterns = [
    path('customerdetails/',views.customersignup,name='booking'),
    path('newsale/',views.addsale,name="sales"),
    path('addinventory/',views.inventory_add, name ="add_inventory"),
    path('addaccessories/<slug>/',views.accessories, name="add_accessories"),
    path('alterinventory/',views.inventory_alter, name = "alter_inventory")
]
#path('updateinventory/',views.inventory_update, name = "inventory_update")
