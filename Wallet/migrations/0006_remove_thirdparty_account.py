# Generated by Django 4.0.6 on 2022-08-19 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Wallet', '0005_remove_transaction_receipt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thirdparty',
            name='account',
        ),
    ]