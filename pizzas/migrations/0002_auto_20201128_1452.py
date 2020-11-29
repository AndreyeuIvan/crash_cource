# Generated by Django 3.1.3 on 2020-11-28 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topping',
            name='pizza',
        ),
        migrations.AddField(
            model_name='pizza',
            name='size',
            field=models.CharField(choices=[('P', 4), ('S', 6), ('M', 8), ('L', 12), ('XL', 16)], default='P', max_length=10),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(to='pizzas.Topping'),
        ),
        migrations.AlterField(
            model_name='topping',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='ToppingAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(choices=[(1, 'Regular'), (2, 'Double'), (3, 'Triple')], default=1)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topping_amounts', to='pizzas.pizza')),
                ('toppings', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='topping_amounts', to='pizzas.topping')),
            ],
        ),
    ]