from . import views
from django.urls import path, re_path


urlpatterns = [
	#Home page
	#re_path(r'^$', views.home, name='learning_logs/home'),
		
	# Show all topics.
	re_path(r'^$', views.topics, name='topics'),
	# Detail page for a single topic
	re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic , name='topic'),
	#Page for adding a new topic
	re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
	#Page for adding a new entry
	re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
	re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
		]