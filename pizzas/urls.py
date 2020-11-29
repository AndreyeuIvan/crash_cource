from . import views
from django.urls import path, re_path


urlpatterns = [
	#Home page
	re_path(r'^$', views.pizzas, name='pizzas'),
	re_path(r'^pizza/(?P<pizza_id>\d+)/$', views.pizza, name='pizza'),
		]