from django.contrib import admin
from accounts.models import sales,customer,inventory,color,accessory
# Register your models here.
admin.site.register(sales)
admin.site.register(customer)
admin.site.register(inventory)
admin.site.register(color)
admin.site.register(accessory)
