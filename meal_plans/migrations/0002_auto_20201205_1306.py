# Generated by Django 3.1.3 on 2020-12-05 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal_plans', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizzas',
            name='size',
        ),
        migrations.AddField(
            model_name='pizzas',
            name='size',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='size', to='meal_plans.sizes'),
            preserve_default=False,
        ),
    ]
