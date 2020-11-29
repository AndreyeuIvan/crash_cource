from django.shortcuts import render
from .models import Pizza, Topping, ToppingAmount

# Create your views here.

def pizzas(request):
	"""Show all pizzas in pizzeria"""
	pizzas = Pizza.objects.all()
	context = {'pizzas': pizzas}
	return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
	"""Show details of toppings in pizza"""
	pizza = Pizza.objects.get(id=pizza_id)
	toppings = ToppingAmount.objects.get(pizza=pizza)
	context = {'pizza' : pizza, 'toppings': toppings}
	return render(request, 'pizzas/pizza.html', context)