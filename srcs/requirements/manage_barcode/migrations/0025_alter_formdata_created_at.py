# Generated by Django 4.1.13 on 2024-08-09 10:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_barcode', '0024_formdata_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 9, 10, 41, 27, 757836)),
        ),
    ]
