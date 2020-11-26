from django.db import models


class Pizza(models.Model):
	"""18-4 exercise, practising django"""
	name = models.CharField(max_length=200)

	def __str__(self):
		"""Return a string representation """
		return self.name


class Topping(models.Model):
	"""Something specific about Pizza will defined here"""
	pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)

	def __str__(self):
		"""Return a string representation """
		return self.name[:55]
		
