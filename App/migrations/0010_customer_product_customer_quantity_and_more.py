# Generated by Django 5.1 on 2024-10-25 15:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_customer_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='App.products'),
        ),
        migrations.AddField(
            model_name='customer',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.CharField(max_length=200, null=True),
        ),
    ]