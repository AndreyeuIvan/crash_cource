from django.shortcuts import render

# Create your views here.
def home(request):
	"""Here I want to present my meal plan html"""
	return render(request, 'meal_plans/base.html')
