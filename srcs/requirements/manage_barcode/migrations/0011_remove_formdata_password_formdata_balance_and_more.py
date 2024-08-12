# Generated by Django 4.1.13 on 2024-07-27 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_barcode', '0010_wallet_tickets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formdata',
            name='password',
        ),
        migrations.AddField(
            model_name='formdata',
            name='balance',
            field=models.IntegerField(default=500),
        ),
        migrations.DeleteModel(
            name='Wallet',
        ),
    ]
