# Generated by Django 4.1.3 on 2022-12-31 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_remove_order_data_ordered'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='service_price',
            new_name='service_prices',
        ),
    ]