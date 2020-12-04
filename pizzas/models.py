from django.db import models


class Topping(models.Model):
    """Something specific about Pizza will defined here"""
    name = models.CharField(max_length=100)
    

    def __str__(self):
        """Return a string representation """
        return self.name


class Pizza(models.Model):
    """18-4 exercise, practising django"""
    PIZZA_SIZES = (
        ('P', 4),
        ('S', 6),
        ('M', 8),
        ('L', 12),
        ('XL', 16),
        )
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=10, choices=PIZZA_SIZES, default=PIZZA_SIZES[0][0])
    toppings = models.ManyToManyField(Topping,through='ToppingAmount', related_name='pizzas')

    def __str__(self):
        """Return a string representation """
        return self.name


class ToppingAmount(models.Model):
    """Here we will defien amount of toppics"""
    AMOUNT_CHOICES = (
        (1, 'Regular'),
        (2, 'Double'),
        (3, 'Triple'),
    )
    pizza = models.ForeignKey(Pizza, related_name='topping_amounts', on_delete=models.CASCADE)
    toppings = models.ForeignKey('Topping', related_name='topping_amounts', on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.IntegerField(choices=AMOUNT_CHOICES, default=AMOUNT_CHOICES[0][0])

    def __str__(self):
        """Return a string representation """
        return self.pizza.name
