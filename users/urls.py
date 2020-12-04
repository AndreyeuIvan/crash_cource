"""Defines URL patterns for users"""


from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views


from . import views


urlpatterns = [
	# Login page
	re_path(r'^login/$', auth_views.LoginView.as_view(template_name='users/users.html'), name='login'),
	re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
	#Register page.
	re_path(r'^register/$', views.register, name='register'),
	]