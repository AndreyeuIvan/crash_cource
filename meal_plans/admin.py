from django.contrib import admin
from .models import Pizzas, Toppings, Sizes, ToppingAmount
# Register your models here.

admin.site.register(Pizzas)
admin.site.register(Toppings)
admin.site.register(Sizes)
admin.site.register(ToppingAmount)