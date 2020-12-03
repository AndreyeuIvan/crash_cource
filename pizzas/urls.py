from . import views
from django.urls import path, re_path


urlpatterns = [
	#Home page
	re_path(r'^$', views.pizzas, name='pizzas'),
	re_path(r'^pizza/(?P<pizza_id>\d+)/$', views.pizza, name='pizza'),
	re_path(r'^new_pizza/$', views.new_pizza, name='new_pizza'),
	re_path(r'^new_topping/(?P<topping_id>\d+)/$', views.new_topping, name='new_topping'),
		]