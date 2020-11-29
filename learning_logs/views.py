from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import TopicForm, EntryForm
from .models import Topic


def home(request):
	"""The home page for LEarning Log"""
	return render(request, 'learning_logs/index.html')

def topics(request):
	"""Show all topics."""
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
	"""Show a single topic and all its entries"""
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
	"""Add a new topic"""
	if request.method != 'POST':
		#No data submitted; create a blank form.
		form = TopicForm()
	else:
		#POST data submitted; process data.
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return topics(request)

	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	if request.method != 'POST':
		form = EntryForm()
	else:
		form = EntryForm(request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('topic', args =[topic_id]))
	context = {'topic': topic, 'form':form}
	return render(request, 'learning_logs/new_entry.html', context)