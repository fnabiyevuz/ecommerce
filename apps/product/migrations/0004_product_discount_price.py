# Generated by Django 4.2 on 2023-04-18 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_category_options_remove_product_customisation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Price'),
        ),
    ]