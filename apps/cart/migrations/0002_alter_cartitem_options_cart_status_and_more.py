# Generated by Django 4.2 on 2023-04-19 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'Cart Item', 'verbose_name_plural': 'Cart Items'},
        ),
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('NEW', 'New'), ('ORDERED', 'Ordered')], default='NEW', max_length=10, verbose_name='Cart status'),
        ),
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart', 'product')},
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='status',
        ),
    ]
