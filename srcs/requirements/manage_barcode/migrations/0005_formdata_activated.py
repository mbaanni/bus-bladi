# Generated by Django 4.1.13 on 2024-07-23 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_barcode', '0004_alter_formdata_tel'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdata',
            name='activated',
            field=models.BooleanField(default=False),
        ),
    ]
