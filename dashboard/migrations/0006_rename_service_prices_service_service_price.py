# Generated by Django 4.1.3 on 2022-12-31 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_rename_service_price_service_service_prices'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='service_prices',
            new_name='service_price',
        ),
    ]