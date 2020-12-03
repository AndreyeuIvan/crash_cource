from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import PizzaForm, ToppingForm
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


def new_pizza(request):
	if request.method != 'POST':
		form = PizzaForm()
	else:
		form = PizzaForm(request.POST)
		if form.is_valid():
			form.save()
			return pizzas(request)
	context = {'form': form}
	return render(request, 'pizzas/new_pizza.html', context)


def new_topping(request, pizza_id):
	pizza = Pizza.objects.get(id=pizza_id)
	if request.method != 'POST':
		form = ToppingForm()
	else:
		form = ToppingForm(request.POST)
		if form.is_valid():
			new_topping = form.save(commit=False)
			new_topping.pizza = pizza
			new_topping.save()
			return HttpResponseRedirect(reverse('pizzas:pizza', args=[pizza_id]))
	context = {'topic': topic,'form': form}
	return render(request, 'pizzas/new_pizza.html', context)
