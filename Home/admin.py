from django.contrib import admin

# Register your models here.
from Home.models import Combos, Pizzas, Beverages, Orders, Featured
admin.site.register(Combos)
admin.site.register(Pizzas)
admin.site.register(Beverages)
admin.site.register(Orders)
admin.site.register(Featured)
