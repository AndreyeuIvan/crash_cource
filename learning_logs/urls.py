from . import views
from django.urls import path


urlpatterns = [
	#Home page
	path(r'', views.index, name='index'),
		]