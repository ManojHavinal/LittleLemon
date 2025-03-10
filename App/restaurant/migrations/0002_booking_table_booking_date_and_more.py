# Generated by Django 5.0.7 on 2024-07-22 10:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_table',
            name='Booking_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='booking_table',
            name='no_of_guests',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='menu_table',
            name='Inventory',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='menu_table',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
