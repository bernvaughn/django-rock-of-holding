# Generated by Django 4.0.4 on 2022-07-26 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_inventory_maximum_weight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iteminstance',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]