# Generated by Django 4.2 on 2023-04-19 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20230419_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Quantity'),
        ),
    ]
