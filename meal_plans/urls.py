from . import views
from django.urls import path, re_path


urlpatterns = [
	#Home page
	re_path(r'^$', views.home, name='meal_plans/home'),
		]