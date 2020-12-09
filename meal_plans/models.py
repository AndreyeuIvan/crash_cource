from django.db import models

# Create your models here.
'''pizza		sizes		toppings
size        name        name
						amount
'price'		'price'
toppings
'amount'
'''


class Sizes(models.Model):
    PIZZA_SIZES = (
        ('P', 4),
        ('S', 6),
        ('M', 8),
        ('L', 12),
        ('XL', 16),
    )
    name = models.CharField(max_length=10, choices=PIZZA_SIZES, default=PIZZA_SIZES[0][0])

    def __str__(self):
        return self.name


class ToppingAmount(models.Model):
    """Here we will store amount of toppings"""
    AMOUNT_CHOICES = (
        (1, 'Regular'),
        (2, 'Double'),
        (3, 'Triple'),
    )
    amount = models.IntegerField(choices=AMOUNT_CHOICES, default=AMOUNT_CHOICES[0][0])


class Toppings(models.Model):
    name = models.CharField(max_length=30)
    #amount = models.ManyToManyField(Amount, related_name='amount_of_toppings')

    def __str__(self):
        return self.name


class Pizzas(models.Model):
    name = models.CharField(max_length=30)
    toppings = models.ManyToManyField(Toppings, related_name='topping')
    amount = models.ForeignKey(ToppingAmount, on_delete=models.CASCADE)
    size = models.ForeignKey(Sizes, related_name='size', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
