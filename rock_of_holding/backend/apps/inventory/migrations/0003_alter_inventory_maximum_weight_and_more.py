# Generated by Django 4.0.4 on 2022-07-26 20:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_inventory_hidden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='maximum_weight',
            field=models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='itemdefinition',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='itemdefinition',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
