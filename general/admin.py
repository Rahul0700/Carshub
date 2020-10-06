from django.contrib import admin
from accounts.models import sales,customer,inventory,accessories
# Register your models here.
admin.site.register(sales)
admin.site.register(customer)
admin.site.register(inventory)
admin.site.register(accessories)
