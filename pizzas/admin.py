from django.contrib import admin

# Register your models here.
from pizzas.models import Pizza, Topping

# Register your models here.
admin.site.register(Topping)
admin.site.register(Pizza)