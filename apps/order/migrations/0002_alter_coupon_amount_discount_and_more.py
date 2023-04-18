# Generated by Django 4.2 on 2023-04-17 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_cart_session_key_alter_cart_user_and_more'),
        ('common', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='amount_discount',
            field=models.PositiveIntegerField(default=0, verbose_name='Amount discount'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='Is available?'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='min_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Minimal amount'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_orders', to='cart.cart', verbose_name='Cart'),
        ),
        migrations.AlterField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coupon_orders', to='order.coupon', verbose_name='Coupon'),
        ),
        migrations.AlterField(
            model_name='order',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_district', to='common.district', verbose_name='District'),
        ),
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='Full name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='Note'),
        ),
        migrations.AlterField(
            model_name='order',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_region', to='common.region', verbose_name='Region'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Total'),
        ),
    ]